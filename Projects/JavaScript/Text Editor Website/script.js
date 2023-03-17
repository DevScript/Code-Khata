const textArea = document.getElementById('content');
const characterCount = document.getElementById('cCount');
const wordCount = document.getElementById('wCount');

textArea.oninput = () => {       //execute this method when anything is input in textarea
    let characters = textArea.value;
    characterCount.textContent = characters.replace(/\s/g, '').length;  //getting character.length where character is the whole vlaue in text area and then using regular expression to not count spaces

    let words = textArea.value;
    wordCount.textContent = words.trim().split(/\s+/).length;

    if (characters.length == 0) wordCount.textContent = 0;
};