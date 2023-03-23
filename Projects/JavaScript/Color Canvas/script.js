const canvas = document.querySelector('#draw');
const ctx = canvas.getContext('2d');    //we draw on context, ctx will be drawing all the lines

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

ctx.strokeStyle = '#BADA55';    //color of stroke
ctx.lineJoin = 'round'; //line ends with circle when join
ctx.lineCap = 'round';  //lines end with rounded tip    //if you switch off by commenting this one you will get a funky style line try it
ctx.lineWidth = 10;
// ctx.globalCompositeOperation = 'multiply';   //allows color blend when lines overlap

let isDrawing = false;
let lastX = 0;  //where we start and where we stop
let lastY = 0;
let hue =0;     //  0 is red    //we will be playing with colors for our stroke and make them colorful


function draw(e){
if(!isDrawing) return;  //stop the function from running when they are not moused down
ctx.strokeStyle= `hsl(${hue}, 100%, 50%)`;   //100%saturation and 50% lightness  //hsl is hue travelling from RGB and back to R like the angle circle from 0 to 360 and back to 0    //read more here - https://mothereffinghsl.com/
ctx.beginPath();
ctx.moveTo(lastX, lastY);   //start from
ctx.lineTo(e.offsetX, e.offsetY);   //go to wherever users mouse is going
ctx.stroke();
lastX=e.offsetX;    //can be written in one line trick --- [lastX, lastY] = [e.offsetX, e.offsetY];
lastY=e.offsetY;
hue++;  //change color value    once it goes over 360 its starts again from red
//we can also play with line width in the same way by giving it vlaue smae as hue and using if(hue>360) hue=0; start again
}

canvas.addEventListener('mousedown', (e) => {   //mousedown is when left mouse button is pressed
    isDrawing=true;
    [lastX, lastY] = [e.offsetX, e.offsetY];    //update last X and Y to where it is clicked
});

canvas.addEventListener('mousemove', draw);
canvas.addEventListener('mouseup', () => isDrawing=false);
canvas.addEventListener('mouseout', () => isDrawing=false); //when mouse goes out of screen
