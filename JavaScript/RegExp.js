/* This file contains all the information about RegExp in JavaScript as a Beginer */

/*Regular Expressions: 

- A regular expression or RegExp is a small programming language that helps to find pattern in data. 
A RegExp can be used to check if some pattern exists in a different data types. 

Note: To use RegExp in JavaScript either we use RegExp constructor or we can declare a RegExp pattern using two forward slashes followed by a flag.

To declare a string we use a single quote, double quote a backtick while to declare a regular expression we use two forward slashes and an optional flag. 

RegExp Parameters: A regular expression takes two parameters. One required search pattern and an optional flag.

Pattern: 
A pattern could be a text or any form of pattern which some sort of similarity. 
For instance the word spam in an email could be a pattern we are interested to look for in an email 
    or 
a phone number format number might be our interest to look for.

Flags are optional parameters in a regular expression which determine the type of searching. Let us see some of the flags:
        g: a global flag which means looking for a pattern in whole text
        i: case insensitive flag (searches for both lowercase and uppercase)
        m: multiline

Other flags include: s, u, y
*/

//***********Code***********/

// Syntax Example: 
let pattern = 'Hacktober'
let flag = 'gi' //g: global & i: case insensitive
let regExpPattern = new RegExp(pattern, flag) //pattern:String, flag: a flag or a combination of flags


// Declaring a regex pattern using RegExp object. Writing the pattern and the flag inside the RegExp constructor
let regex = new RegExp('anyword', 'gim') //g: global, i: case insensitive, m: multiline


// creating a RegExp without its constructor
let regexWO = /fest/gi; //(pattern, flag)


// RegExp methods

// 1. to test a pattern, i.e testing for a match
// test(), Tests for a match in a string, it returns a boolean i.e true or false

// example: 
const str = 'i am full of cash'
const str2 = 'i am fUlL of cash'
const pattern1 = /full/g;
console.log(pattern1.test(str)); //true
console.log(pattern1.test(str2)); //false, cuz the we did'nt add a case insensitive flag


// 2. match(): Returns an array containing all of the matches, including capturing groups, or null if no match is found.
// If we do not use a global flag, match() returns an array containing the pattern, index, input and group.
// example: 
const str3 = 'i am full of cash and full of water'
const withoutG = /full/
const withG = /full/g

//without g flag
console.log(str3.match(withoutG))
// without g flag it returned pattern, groups which is unidentified, index and input
// output:
// 0: "full"
// groups: undefined
// index: 5
// input: "i am full of cash and full of water"
// length: 1

// with g flag
console.log(str3.match(withG))
// output:
// with g flag, it will simply return the array of matches.
// output:
// 0: "full"
// 1: "full"
// length: 2


// 3. search(): Tests for a match in a string. It returns the index of the match, or -1 if the search fails.
console.log(str3.search(withG)) //5 //it will return the index of the first match it finds 

console.log('this sentence will not contain the pattern'.search(withG)) //-1 cuz there is no match found, i.e there is no 'full' in this string


//Replacing a substring
// 4. replace(): Executes a search for a match in a string, and replaces the matched substring with a replacement substring.
// example: 
const txt = 'Python is the most beautiful language that a human begin has ever created.\
I recommend python for a first programming language'
matchReplaced = txt.replace(/Python|python/, 'JavaScript') //with no flag
//only replaces the first match it finds
console.log(matchReplaced) //JavaScript is the most beautiful language that a human begin has ever created.I recommend python for a first programming language

// note: we can also include two or more patterns using a OR operator like this
// patternWithOR = /full|Full|FULL/g


//                           pattern to be replaced, replacement
matchReplacedWithG = txt.replace(/Python|python/g, 'JavaScript')
//this will replace all the matches from the whole text
console.log(matchReplacedWithG) //JavaScript is the most beautiful language that a human begin has ever created.I recommend JavaScript for a first programming language

//this will replace all the matches from the whole text, it is also case insensitive
matchReplacedWithGI = txt.replace(/python/gi, 'JavaScript')
//this will replace all the matches from the whole text
console.log(matchReplacedWithG) //JavaScript is the most beautiful language that a human begin has ever created.I recommend JavaScript for a first programming language

// Example Scenario of replace()
// To remove % sign from a text
const txt2 = '%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing.\
T%he%re i%s n%o%th%ing as m%ore r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing \
p%e%o%ple.\
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs.\
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher.'

//replaces the % sign with empty string
matches = txt2.replace(/%/g, '')
console.log(matches) //I am teacher and  I love teaching.There is nothing as more rewarding as educating and empowering people.I found teaching more interesting than any other jobs.Does this motivate you to be a teacher.


// PS: RegExp is a powerful tool, thought it contains hundreds of function which we all cannot memorize, however you should know the 
// basics of RegExp as a well versed developer.

//////Note: 
// To learn more and to create different RegExp patterns for different use cases:
//  https://regex101.com/

// The main goal of using RegExp is to extract and clearn any kind of text to make some meaning out of it \\
