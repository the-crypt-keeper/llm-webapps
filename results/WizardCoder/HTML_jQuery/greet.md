```html
<!DOCTYPE html>
<html>
<head>
	<title>Greetings</title>
	<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
	<script>
		$(document).ready(function(){
			$("#greet").click(function(){
				var name = $("#name").val();
				var language = $("#language").val();
				if(language == "English"){
					alert("Hello " + name + "!");
				}
				else if(language == "French"){
					alert("Bonjour " + name + "!");
				}
				else if(language == "Spanish"){
					alert("Hola " + name + "!");
				}
			});
		});
	</script>
</head>
<body>
	<label for="language">Select Language:</label>
	<select id="language">
		<option value="English">English</option>
		<option value="French">French</option>
		<option value="Spanish">Spanish</option>
	</select>
	<br><br>
	<label for="name">Enter Name:</label>
	<input type="text" id="name" name="name"><br><br>
	<button id="greet">Greet</button>
</body>
</html>
```

In this application, we have used jQuery library to select the language and name from the drop-down selection box and text entry field respectively. When the button is clicked, we have used the `val()` method to get the selected language and name and then used an `if-else` statement to greet the user in the selected language.