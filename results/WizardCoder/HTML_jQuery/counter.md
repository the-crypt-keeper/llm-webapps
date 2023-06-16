```html
<!DOCTYPE html>
<html>
<head>
	<title>Counter App</title>
	<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
	<script>
		$(document).ready(function(){
			var counter = 1;
			$('#counter').text(counter);

			$('#increase').click(function(){
				counter++;
				if(counter < 1){
					counter = 1;
				}
				$('#counter').text(counter);
			});

			$('#decrease').click(function(){
				counter--;
				if(counter < 1){
					counter = 1;
				}
				$('#counter').text(counter);
			});

			$('#reset').click(function(){
				counter = 1;
				$('#counter').text(counter);
			});
		});
	</script>
</head>
<body>
	<h1>Counter App</h1>
	<p>Current Count: <span id="counter">1</span></p>
	<button id="increase">Increase</button>
	<button id="decrease">Decrease</button>
	<button id="reset">Reset</button>
</body>
</html>
```

In this application, we have used jQuery to manipulate the DOM and handle the button clicks. We have also used a variable `counter` to keep track of the current count. The `$(document).ready()` function ensures that the code inside it is executed only after the DOM is fully loaded.

The `$('#counter').text(counter);` line sets the text of the `span` element with `id="counter"` to the current value of `counter`.

The `$('#increase').click(function(){...});` line attaches a click event listener to the `button` element with `id="increase"`. When the button is clicked, the function inside the curly braces is executed. The `counter` variable is incremented by 1, and the `if` statement checks if the counter is less than 1. If it is, the counter is set back to 1. Finally, the `$('#counter').text(counter);` line updates the text of the `span` element with `id="counter"` to the new value of `counter`.

The `$('#decrease').click(function(){...});` line is similar to the `$('#increase').click(function(){...});` line, but decrements the `counter` variable instead of incrementing it.

The `$('#reset').click(function(){...});` line sets the `counter` variable back to 1, and updates the text of the `span` element with `id="counter"` to reflect the new value of `counter`.