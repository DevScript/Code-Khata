const checkboxes = document.querySelectorAll('.inbox input[type="checkbox"]');
let lastChecked;

function handleCheck(e) {
    //check if shift key was pressed or not and check that they are checking it
    let inBetween = false;
    if (e.shiftKey && this.checked) {
        checkboxes.forEach(checkbox => {
            //console.log(checkbox);//loop over ever single box
            if (checkbox === this || checkbox === lastChecked) {
                inBetween = !inBetween;     //same as inBetween = true;
                //console.log('Starting to check them in between');
            }
            if (inBetween) 
            {
                checkbox.checked = true;
            }
        });
    }
    lastChecked = this;
}

checkboxes.forEach(checkbox => checkbox.addEventListener('click', handleCheck));