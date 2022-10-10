import 'package:flutter/material.dart';
import 'package:yourapp/res/app_colors.dart';

class AuthField extends StatelessWidget {
  final TextEditingController controller;
  final String label;
  final String hintText;
  final TextInputAction? textInputAction;
  final TextInputType? keyboardType;
  final bool obscureText;
  final IconData? iconData;
  final VoidCallback? iconPressed;
  final bool isRequired;
  const AuthField({
    super.key,
    required this.controller,
    required this.label,
    required this.hintText,
    this.textInputAction,
    this.keyboardType,
    this.obscureText = false,
    this.iconData,
    this.iconPressed,
    this.isRequired = true,
  });

  @override
  Widget build(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Row(
          children: [
            Text(
              label,
              style: const TextStyle(
                color: Colors.black,
                fontSize: 14,
                fontWeight: FontWeight.bold,
              ),
            ),
            Visibility(
              visible: isRequired,
              child: const Text(
                '*',
                style: TextStyle(
                  color: Colors.red,
                  fontSize: 14,
                  fontWeight: FontWeight.bold,
                ),
              ),
            ),
          ],
        ),
        const SizedBox(height: 10),
        Container(
          height: 48,
          alignment: Alignment.center,
          decoration: BoxDecoration(
            border: Border.all(width: 0.4, color: AppColors.greyTextColor),
            borderRadius: BorderRadius.circular(12),
          ),
          child: iconData == null
              ? _buildField()
              : Row(
                  children: [
                    Expanded(child: _buildField()),
                    InkWell(
                      onTap: iconPressed,
                      child: Icon(
                        iconData,
                        color: AppColors.primaryColor,
                      ),
                    ),
                    const SizedBox(width: 12),
                  ],
                ),
        ),
      ],
    );
  }

  Widget _buildField() {
    return TextField(
      cursorColor: AppColors.primaryColor,
      controller: controller,
      textInputAction: textInputAction,
      obscureText: obscureText,
      keyboardType: keyboardType,
      decoration: InputDecoration(
        border: InputBorder.none,
        hintText: hintText,
        contentPadding:
            const EdgeInsets.symmetric(horizontal: 12).copyWith(bottom: 2),
        hintStyle: const TextStyle(
          color: AppColors.hintColor,
          fontSize: 12,
        ),
      ),
    );
  }
}
