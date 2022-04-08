function dynamicResizing(width) {
	var min_width_for_wide_title = 600
	console.log("Width is");
	console.log(width);

	if (width < min_width_for_wide_title) {
		// Background images
		$("#mainpage_wide").addClass("hidden")
		$("#mainpage_thin").removeClass("hidden")

		// Font sizes
		$("#tt_1_wide").addClass("hidden")
		$("#tt_2_wide").addClass("hidden")
		$("#tt_1_thin").removeClass("hidden")
		$("#tt_2_thin").removeClass("hidden")
	} else {
		// Background images
		$("#mainpage_wide").removeClass("hidden")
		$("#mainpage_thin").addClass("hidden")

		// Font sizes
		$("#tt_1_thin").addClass("hidden")
		$("#tt_2_thin").addClass("hidden")
		$("#tt_1_wide").removeClass("hidden")
		$("#tt_2_wide").removeClass("hidden")
	}
}

// Handle all the dynamic resizing options
$(window).resize(function() {
	dynamicResizing($(this).width());
});

window.onload = function() {
	dynamicResizing($(this).width());
}
