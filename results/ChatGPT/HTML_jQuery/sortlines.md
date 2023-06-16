<!DOCTYPE html>
<html>
<head>
	<title>Text Sorter</title>
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
	<script>
		$(document).ready(function(){
			$("#processBtn").click(function(){
				var inputText = $("#inputTextArea").val();
				var lines = inputText.split("\n");
				lines.sort();
				var uniqueLines = [...new Set(lines)];
				var outputText = uniqueLines.join("\n");
				$("#outputTextArea").val(outputText);
			});
		});
	</script>
</head>
<body>
	<h1>Text Sorter</h1>
	<div>
		<label for="inputTextArea">Input Text:</label><br>
		<textarea id="inputTextArea" rows="10" cols="50"></textarea>
	</div>
	<div>
		<label for="outputTextArea">Output Text:</label><br>
		<textarea id="outputTextArea" rows="10" cols="50" readonly></textarea>
	</div>
	<button id="processBtn">Process</button>
</body>
</html>