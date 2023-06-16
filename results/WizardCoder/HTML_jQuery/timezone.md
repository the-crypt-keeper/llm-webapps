```html
<!DOCTYPE html>
<html>
<head>
	<title>Time Zone Converter</title>
	<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
	<script>
		$(document).ready(function(){
			// Time Zone dropdown list
			var timeZones = [
				{name: "UTC", offset: "+00:00"},
				{name: "GMT", offset: "+00:00"},
				{name: "US/Eastern", offset: "-05:00"},
				{name: "US/Central", offset: "-06:00"},
				{name: "US/Mountain", offset: "-07:00"},
				{name: "US/Pacific", offset: "-08:00"}
			];

			// Create dropdown list
			var select = $("<select>");
			$.each(timeZones, function(index, value){
				var option = $("<option>").val(value.offset).text(value.name);
				select.append(option);
			});

			// Append dropdown list to body
			$("body").append(select);

			// Display current time in selected time zone
			select.change(function(){
				var selectedTimeZone = $(this).val();
				var currentTime = new Date();
				var timeZoneOffset = selectedTimeZone.substring(1, 3) * 60 + selectedTimeZone.substring(4, 6) * 1;
				var timeZoneHours = Math.floor(timeZoneOffset / 60);
				var timeZoneMinutes = timeZoneOffset % 60;
				var timeZoneOffsetString = (timeZoneHours < 0? "-" : "+") + ("0" + Math.abs(timeZoneHours)).slice(-2) + ":" + ("0" + timeZoneMinutes).slice(-2);
				var timeZoneDate = new Date(currentTime.toLocaleString("en-US", {timeZone: timeZoneOffsetString}));
				var timeZoneTime = timeZoneDate.toLocaleTimeString("en-US", {timeZone: timeZoneOffsetString});
				$("#current-time").text(timeZoneTime);
			});
		});
	</script>
</head>
<body>
	<h1>Time Zone Converter</h1>
	<p>Select a time zone:</p>
	<div id="current-time"></div>
</body>
</html>
```

This HTML code creates a dropdown list of time zones using jQuery and displays the current time in the selected time zone. The dropdown list is created using a loop that iterates over an array of objects containing the time zone name and offset. The dropdown list is appended to the body of the HTML document using the `append()` method. The `change()` method is used to update the current time when the user selects a new time zone. The current time is calculated using the `Date()` constructor and the `toLocaleString()` and `toLocaleTimeString()` methods. The time zone offset is calculated using string manipulation and the `substring()` method. The time zone offset is then used to create a new `Date()` object with the appropriate time zone offset. Finally, the current time is displayed in the `div` element with the id `current-time` using the `text()` method.