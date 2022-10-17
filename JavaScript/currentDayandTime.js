// DISPLAYING CURRENT DAY AND TIME          
var now = new Date();
//console.log(now);
var day = now.getDay();
//console.log(day);
    switch (day) {
        case 0:
            day = "Sunday";
            break;
        case 1:
            day = "Monday";
            break;
        case 2:
            day = "Tuesday";
            break;
        case 3:
            day = "Wednesday";
            break;
        case 4:
            day = "Thursday";
            break;
        case 5:
            day = "Friday";
            break;
        case 6:
            day = "Saturday";
            break;
        default:
            day = "Invalid";
            break;
            }

    var hr = now.getHours();
    var min = now.getMinutes();
    var sec = now.getSeconds();
    document.write("Today is : " + day);
    document.write("<br>Current Time :" + hr + " A.M : " + min + " : " + sec);
