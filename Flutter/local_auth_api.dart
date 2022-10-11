import 'package:flutter/services.dart';
import 'package:local_auth/local_auth.dart';

class LocalAuthApi {
  static final _auth = LocalAuthentication();

  static Future<bool> hasBiometrics() async {
    try {
      return await _auth.canCheckBiometrics;
    } on PlatformException {
      return false;
    }
  }

  static Future<List<BiometricType>> getBiometrics() async {
    try {
      return await _auth.getAvailableBiometrics();
    } on PlatformException {
      return <BiometricType>[];
    }
  }

  static Future<bool> authenticate({required String localizedReason}) async {
    final isAvailable = await hasBiometrics();
    if (!isAvailable) return false;

    try {
      return await _auth.authenticate(
        localizedReason: localizedReason,
        options: const AuthenticationOptions(
          useErrorDialogs: true,
          stickyAuth: true,
          biometricOnly: true,
        ),
      );
    } on PlatformException {
      return false;
    }
  }

  static Future<bool> hasFingerprint() async {
    try {
      final isAvailable = await hasBiometrics();
      if (!isAvailable) return false;
      final biometrics = await getBiometrics();

      final hasFingerprint = biometrics.contains(BiometricType.fingerprint);
      return hasFingerprint;
    } catch (e) {
      return false;
    }
  }

  static Future<bool> hasFaceId() async {
    try {
      final isAvailable = await hasBiometrics();
      if (!isAvailable) return false;
      final biometrics = await getBiometrics();

      final hasFaceId = biometrics.contains(BiometricType.face);
      return hasFaceId;
    } catch (e) {
      return false;
    }
  }
}
