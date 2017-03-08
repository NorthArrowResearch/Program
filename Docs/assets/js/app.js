// Custom JS Goes HERE
$(document).ready(function (){

	$(document).foundation();

	/**
	 * Recursively build a menu system
	 * @param  {[type]}
	 * @param  {[type]}
	 * @param  {[type]}
	 * @return {[type]}
	 */
	function menurecurse(pages, $menu, currind, depth) {
		// First time run
		if (!$menu) {
			// Append a title
			$menu = ($("<ul class='dropdown menu' data-dropdown-menu></ul>"))
			$menu.append($("<li class='menu-text'>"+NAVTitle+"</li>"));
			currind = "";
			depth = 0;
		}
		else if (currind >= pages) {
			return $menu;
		}
		orderArr = pages[currind].url

		// if deeper go deeper
		if (orderArr > currdepth){

		}
		$inner = $("<ul class='menu vertical' data-dropdown-menu>");
		recurse($inner, currind, depth+1);
		$menu.append($inner);
		
		// Else same
		else{
			$li = $("<li><a href='" + NAVPages[navpage].absurl + "'>" + NAVPages[navpage].title + "</a></li>")
			$menu.append(li)
			currind++;			
		}
	}

	$('#autonav').append(menurecurse(NAVPages));

});

