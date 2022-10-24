let body = document.body;
let h1Tag = document.querySelector("h1");
let weightInput = document.querySelector("input");
let selectTag = document.querySelector("select");
let buttonTag = document.querySelector("button");
let header = document.querySelector("header");
let mainDiv = document.querySelector("main");
let container = document.querySelector(".flex-container");
let imgDiv = document.querySelector(".image");
let img = document.querySelector("img");
let descriptionDiv = document.querySelector(".description");
let descriptionPara = document.querySelector("p");
let massDiv = document.querySelector(".mass");
let regex = /^\d+$/g;

body.style.cssText = "background-image: url(images/galaxy.gif)";
body.style.textAlign = "center";
body.style.fontFamily = "Montserrat";
body.style.color = "beige";

header.style.marginBottom = "20px";

h1Tag.style.color = "beige";
h1Tag.style.fontFamily = "Montserrat";
h1Tag.style.marginBottom = "60px";

// weightInput.style.color = "beige";
weightInput.style.height = "25px";
weightInput.style.fontFamily = "Montserrat";

selectTag.style.color = "grey";
selectTag.style.padding = "5px 10px";
selectTag.style.fontFamily = "Montserrat";

buttonTag.style.color = "beige";
buttonTag.style.padding = "5px 10px";
buttonTag.style.backgroundColor = "#463939";
selectTag.style.fontFamily = "Montserrat";

mainDiv.style.display = "flex";
mainDiv.style.justifyContent = "center";

container.style.backgroundColor = "rgba(255,255,255,0.2)";
container.style.display = "flex";
container.style.flexDirection = "row";
container.style.justifyContent = "center";
container.style.alignItems = "center";
container.style.width = "80%";

img.style.maxWidth = "80%";
img.style.margin = "50px 0px";

descriptionDiv.style.display = "none";
descriptionDiv.style.backgroundColor = "rgba(255,255,255,0.25)";
descriptionDiv.style.padding = "20px 200px";
descriptionDiv.style.margin = "50px 10px";

massDiv.style.borderRadius = "50%";
massDiv.style.padding = "40px 0px";
massDiv.style.backgroundColor = "rgba(255,255,255,0.25)";
massDiv.style.display = "none";

buttonTag.addEventListener("click", (e) => {
  console.log(weightInput.value);
  if (weightInput.value == "") {
    console.log(weightInput.value);
    img.style.display = "none";
    descriptionDiv.style.display = "block";
  } else if (weightInput.value.match(regex) == null) {
    descriptionPara.innerHTML = "Mass must be a number";
    img.style.display = "none";
    descriptionDiv.style.display = "block";
  } else if (selectTag.value == "none") {
    descriptionPara.innerHTML = "You did not choose a planet";
    img.style.display = "none";
    descriptionDiv.style.display = "block";

  } else if (selectTag.value != "none") {

    switch (selectTag.value) {

      case "mercury":
        img.style.display = "block";
        img.src = "images/mercury.png";

        descriptionDiv.style.display = "block";
        descriptionPara.innerHTML =
          "The weight of the object on <strong>MERCURY</strong>";

        massDiv.style.display = "block";
        massDiv.innerHTML = calculateWeight(weightInput.value, 3.7) + " N";

        break;

      case "venus":
        img.style.display = "block";
        img.src = "images/venus.png";
        descriptionDiv.style.display = "block";
        descriptionPara.innerHTML =
          "The weight of the object on <strong>VENUS</strong>";

        massDiv.style.display = "block";
        massDiv.innerHTML = calculateWeight(weightInput.value, 8.87) + " N";

        break;

      case "mars":
        img.style.display = "block";
        img.src = "images/mars.png";
        descriptionDiv.style.display = "block";

        descriptionPara.innerHTML =
          "The weight of the object on <strong>MARS</strong>";

        massDiv.style.display = "block";
        massDiv.innerHTML = calculateWeight(weightInput.value, 3.721) + " N";

        break;

      case "jupiter":
        img.style.display = "block";
        img.src = "images/jupiter.png";
        descriptionDiv.style.display = "block";

        descriptionPara.innerHTML =
          "The weight of the object on <strong>JUPITER</strong>";

        massDiv.style.display = "block";
        massDiv.innerHTML = calculateWeight(weightInput.value, 24.79) + " N";
        break;

      case "earth":
        img.style.display = "block";
        img.src = "images/earth.png";
        descriptionDiv.style.display = "block";

        descriptionPara.innerHTML =
          "The weight of the object on <strong>EARTH</strong>";

        massDiv.style.display = "block";
        massDiv.innerHTML = calculateWeight(weightInput.value, 9.807) + " N";

        break;

      case "saturn":
        img.style.display = "saturn.png";
        descriptionDiv.style.display = "block";

        descriptionPara.innerHTML =
          "The weight of the object on <strong>SATURN</strong>";

        massDiv.style.display = "block";
        massDiv.innerHTML = calculateWeight(weightInput.value, 10.44) + " N";

        break;
      case "uranus":
        img.style.display = "block";
        img.src = "images/uranus.png";
        descriptionDiv.style.display = "block";

        descriptionPara.innerHTML =
          "The weight of the object on <strong>URANUS</strong>";

        massDiv.style.display = "block";
        massDiv.innerHTML = calculateWeight(weightInput.value, 8.87) + " N";

        break;
      case "neptune":
        img.style.display = "block";
        img.src = "images/neptune.png";
        descriptionDiv.style.display = "block";

        descriptionPara.innerHTML =
          "The weight of the object on <strong>NEPTUNE</strong>";

        massDiv.style.display = "block";
        massDiv.innerHTML = calculateWeight(weightInput.value, 11.15) + " N";

        break;

      case "pluto":
        img.style.display = "block";
        img.src = "images/pluto.png";
        descriptionDiv.style.display = "block";
        descriptionPara.innerHTML =
          "The weight of the object on <strong>PLUTO</strong>";

        massDiv.style.display = "block";
        massDiv.innerHTML = calculateWeight(weightInput.value, 0.62) + " N";

        break;
      case "moon":
        img.style.display = "block";
        img.src = "images/moon.png";
        descriptionDiv.style.display = "block";
        descriptionPara.innerHTML =
          "The weight of the object on <strong>MOON</strong>";

        massDiv.style.display = "block";
        massDiv.innerHTML = calculateWeight(weightInput.value, 1.62) + " N";

        break;

      default:
        break;
    }
  }
});

let calculateWeight = (mass, g) => parseFloat(mass * g).toFixed(2);
