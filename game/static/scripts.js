function dynamicResizing(width) {
	var min_width_for_wide_title = 600

	if (width < min_width_for_wide_title) {
		console.log("tall image");
		// Background images
		$("#mainpage_wide").addClass("hidden")
		$("#mainpage_tall").removeClass("hidden")

		// Font sizes
		$("#tt_1_wide").addClass("hidden")
		$("#tt_2_wide").addClass("hidden")
		$("#tt_1_tall").removeClass("hidden")
		$("#tt_2_tall").removeClass("hidden")
	} else {
		// Background images
		$("#mainpage_wide").removeClass("hidden")
		$("#mainpage_tall").addClass("hidden")

		// Font sizes
		$("#tt_1_tall").addClass("hidden")
		$("#tt_2_tall").addClass("hidden")
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
