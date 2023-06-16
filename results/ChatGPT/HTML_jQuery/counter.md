<!DOCTYPE html>
<html>
<head>
	<title>Counter App</title>
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
	<style type="text/css">
		#counter {
			font-size: 100px;
			text-align: center;
			margin-top: 50px;
		}
		.row {
			display: flex;
			justify-content: center;
			margin-top: 20px;
		}
		.button {
			padding: 10px 20px;
			margin: 0 10px;
			border-radius: 5px;
			background-color: #4CAF50;
			color: white;
			cursor: pointer;
		}
	</style>
</head>
<body>
	<div id="counter">1</div>
	<div class="row">
		<button class="button" id="increase">Increase</button>
		<button class="button" id="decrease">Decrease</button>
		<button class="button" id="reset">Reset</button>
	</div>

	<script type="text/javascript">
		$(document).ready(function() {
			var counter = 1;

			$("#increase").click(function() {
				counter++;
				$("#counter").html(counter);
			});

			$("#decrease").click(function() {
				if (counter > 1) {
					counter--;
					$("#counter").html(counter);
				}
			});

			$("#reset").click(function() {
				counter = 1;
				$("#counter").html(counter);
			});
		});
	</script>
</body>
</html>