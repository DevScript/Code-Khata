<!DOCTYPE html>
<html>
    <head>

    </head> 

    <body style = "text-align:center;">
        <h1 style = "color:blue;" >
            Capitalize the first letter
        </h1>

        <input id = "input" type="text" name="input"/>
        <button onclick="capitalizeFirstLetter()">
            Click to Capitalize
        </button
        <h3 id = "div" style="color: orange">
        </h3>   
        <script>
        function capitalizeFirstLetter() {
        const input = document.getElementById("input");
        const x = document.getElementById("div");
        const string = input.value;
        x.innerHTML = string[0].toUpperCase() +string.slice(1);
        }
        </script>
    </body>
</html>
