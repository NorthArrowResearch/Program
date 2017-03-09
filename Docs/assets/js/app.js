// Custom JS Goes HERE
$(document).ready(function (){

	/**
	 * Create a tree out of a flat path recursively.
	 * @param  {[type]}
	 * @param  {[type]}
	 * @param  {[type]}
	 * @return {[type]}
	 */
	// Now place each item in the tree
	function treeize(pages){
		var tree = { leaves: [], branches: [] }
		for (i in pages) {
			urlArr = pages[i].url.split('/');
			currLevel = urlArr.shift();
			var pointer = tree;

			// Now loop until we're deep enough
			while (urlArr.length > 1) {
				key = urlArr[0].length == 0 ? "THING" : urlArr[0];
				if (key in pointer.branches){
					pointer = newDir;
				}
				else {
					newDir = { leaves: [], branches: {} }
					pointer.branches[key] = newDir;
					pointer = newDir;
					
				}
				currLevel = urlArr.shift();
			}
			pointer.leaves.push(pages[i]);		
		}
		traverseandsort(tree)
		return tree
	}

	/**
	 * recursively sort a tree by weight then by alphabet
	 * @param  {[type]}
	 * @return {[type]}
	 */
	function traverseandsort(t) {
		// Sort the leaves by weight and then by title
		t.leaves.sort(function(a, b) {

			a.weight = parseInt(a.weight) || 999;
			b.weight = parseInt(b.weight) || 999;
			
			if (a.weight == b.weight) {
				return a.title < b.title ? -1 : (a.title > b.title ? 1 : 0);
			}
			else {
				return a.weight < b.weight ? -1 : (a.weight > b.weight ? 1 : 0);
			}

		});
		// Now go find more branches to sort their leaves
		for (br in t.branches) {
			traverseandsort(t.branches[br])
		}
	}	

	/**
	 * Turn a tree structure from treeize into a topbar
	 * @param  {[type]}
	 * @return {[type]}
	 */
	function topbarize(tree, title) {
		var $topbar = $('<div class="top-bar"></div>');
		var $topbarleft = $('<div class="top-bar-left"></div>');
		$topbar.append($topbarleft);
		var $title = $('<li class="menu-text">Title</li>');

		function menutraverse(t, $mUL) {
			if (!$mUL) {
				$mUL = $('<ul class="dropdown menu" data-dropdown-menu></ul>');
				$mUL.append($title);
			}
			// Now go find more branches to sort their leaves
			for (lf in t.leaves) {
				$li = $('<li><a href="' + t.leaves[lf].absurl + '">' + t.leaves[lf].title + '</a></li>');
				$mUL.append($li);
			}				
			// Now go find more branches to sort their leaves
			for (br in t.branches) {
				$newmLi = $('<li></li>');
				$newmA = $('<a href="#">'+ br +'</a>');
				$newmUl = $('<ul class="menu vertical"></ul>');
				$newmLi.append($newmA);
				$newmLi.append($newmUl);
				$mUL.append($newmLi);
				menutraverse(t.branches[br], $newmUl);
			}
			return $mUL;			
		}

		$topbarleft.append(menutraverse(tree));
		return $topbar
	}

	// Do all the things to get the tree
	tree = treeize(NAVPages);
	$topbar = topbarize(tree);
	console.log(tree);

	$('#topbarnav').append($topbar);

	// Initialize our UI framework
	$(document).foundation();

});

