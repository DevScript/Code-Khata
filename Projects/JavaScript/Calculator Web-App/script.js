let string="";
//Now we want to make all buttons into event listener
let button = document.querySelectorAll('.button');
Array.from(button).forEach((button)=>{
    button.addEventListener('click', (e)=>{

        if(e.target.innerHTML == '='){
            try{
                string = eval(string);
                document.querySelector('input').value = string; 
            }
            catch(e){
                document.querySelector('input').value ="";
            }
        }
        
        else if(e.target.innerHTML == 'CLR'){
            string="";
            document.querySelector('input').value = string;
        }

        else if(e.target.innerHTML == 'DEL'){
            string = string.slice(0,-1);
            document.querySelector('input').value = string;
        }

        else{
        string = string + e.target.innerHTML;
        document.querySelector('input').value = string;
        }
        
    })
})