function leapyear(year)    //function starts from here
{
//A year is leap year if following conditions are satisfied: 
//Year is multiple of 400. Year is multiple of 4 and not multiple of 100.
//three conditions to find out the leap year 
return (year % 100 === 0) ? (year % 400 === 0) : (year % 4 === 0);                                                                    
}
//Checking Results and logging it to the console
console.log(leapyear(2016)); 
console.log(leapyear(2000));
console.log(leapyear(1700));
console.log(leapyear(1800));
console.log(leapyear(100));
