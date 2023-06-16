```html
<!DOCTYPE html>
<html>
<head>
	<title>Sort and Remove Duplicates</title>
	<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
	<script>
		$(document).ready(function(){
			$('#process').click(function(){
				var input = $('#input').val();
				var lines = input.split('\n');
				var uniqueLines = lines.filter(function(item, pos) {
					return lines.indexOf(item) == pos;
				});
				uniqueLines.sort();
				$('#output').val(uniqueLines.join('\n'));
			});
		});
	</script>
</head>
<body>
	<div>
		<textarea id="input" rows="20" cols="50"></textarea>
		<br>
		<button id="process">Process</button>
	</div>
	<div>
		<textarea id="output" rows="20" cols="50" readonly></textarea>
	</div>
</body>
</html>
```

Explanation:

- We start by including the jQuery library in the head section of the HTML document.
- We then use jQuery's `$(document).ready()` function to ensure that the DOM is fully loaded before executing any jQuery code.
- We create a click event listener for the 'Process' button using jQuery's `$('#process').click()` function.
- Inside the click event listener, we get the input text from the input textarea using jQuery's `$('#input').val()` function.
- We then split the input text into lines using the `split()` function and store them in an array called `lines`.
- We use the `filter()` function to remove any duplicates from the `lines` array. This function loops through the array and returns only the elements that are unique, based on their position in the array.
- We then sort the `uniqueLines` array using the `sort()` function.
- Finally, we join the `uniqueLines` array back into a string using the `join()` function and set it as the value of the output textarea using jQuery's `$('#output').val()` function.