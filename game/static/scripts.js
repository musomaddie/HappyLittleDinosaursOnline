// Load the images depending on the page resize.
$(window).resize(function() {
	var width = $(this).width();
	if (width <= 500) {
		$("#mainpage_wide").addClass("hidden")
		$("#mainpage_thin").removeClass("hidden")
	} else {
		$("#mainpage_wide").removeClass("hidden")
		$("#mainpage_thin").addClass("hidden")
	}
});

window.onload = function() {
	if (width <= 500) {
		$("#mainpage_wide").addClass("hidden")
		$("#mainpage_thin").removeClass("hidden")
	} else {
		$("#mainpage_wide").removeClass("hidden")
		$("#mainpage_thin").addClass("hidden")
	}
}
