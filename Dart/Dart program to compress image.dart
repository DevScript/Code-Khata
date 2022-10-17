import 'dart:io';

void main(){
void compressImage() async {
    print('starting compression');
    final tempDir = await getTemporaryDirectory();
    final path = tempDir.path;
    int rand = Random().nextInt(10000);
  
    Im.Image? image = Im.decodeImage(file!.readAsBytesSync());
    Im.copyResize(image!,height: 1080,width: 1080);
  
    var newim2 = new File('$path/img_$rand.jpg')
      ..writeAsBytesSync(Im.encodeJpg(image, quality: 25));
  
  
      file = newim2;
  
    print('done');
  }
