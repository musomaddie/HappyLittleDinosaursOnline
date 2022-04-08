var hiding_class = "hidden"

function hideElement(value) {
	// Hides the given element (by id) from the website by applying the css class
	$(value).addClass(hiding_class)
}

function showElement(value) {
	// Shows the given element (by id) by removing the CSS class.
	// If this is already visible this shouldn't change anything
	$(value).removeClass(hiding_class)
}


function dynamicResizing(width) {
	var min_width_for_wide_title = 600
	var wide_ids = ["#mainpage_wide", "#tt_1_wide", "#tt_2_wide"]
	var tall_ids = ["#mainpage_tall", "#tt_1_tall", "#tt_2_tall"]

	if (width < min_width_for_wide_title) {
		// Tall version
		wide_ids.forEach(hideElement);
		tall_ids.forEach(showElement);
	} else {
		// Wide version
		wide_ids.forEach(showElement);
		tall_ids.forEach(hideElement);
	}
}

// Handle all the dynamic resizing options
$(window).resize(function() {
	dynamicResizing($(this).width());
});

window.onload = function() {
	dynamicResizing($(this).width());
}
