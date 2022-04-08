// Load the images depending on the page resize.
$(window).resize(function() {
	if ($(this).width() <= 500) {
		$("#mainpage_wide").addClass("hidden")
		$("#mainpage_thin").removeClass("hidden")
	} else {
		$("#mainpage_wide").removeClass("hidden")
		$("#mainpage_thin").addClass("hidden")
	}
});

window.onload = function() {
	if ($(this).width() <= 500) {
		$("#mainpage_wide").addClass("hidden")
		$("#mainpage_thin").removeClass("hidden")
	} else {
		$("#mainpage_wide").removeClass("hidden")
		$("#mainpage_thin").addClass("hidden")
	}
}
