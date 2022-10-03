// Email Validation Program to verify email addresses

function validateEmail(email) {
    
    const regex_pattern =    /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    
    if (regex_pattern.test(email)) {
        console.log('The given email address is valid');
    }
    else {
        console.log('The given email address is not valid try another');
    }
}

//Run Function

//Valid
validateEmail('affanali577@gmail.com');

//Invalid
validateEmail('affan@com');