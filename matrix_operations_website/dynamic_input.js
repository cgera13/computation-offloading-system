$(function() {
	
	// Function for creating Matrix 1 input elements
	$('#setDim1').click(function() {
		
		// important use this to remove input elements everytime new dimensions
		// are set (var elem = $('#inputsM1').empty())
		
		var numRows = $('#rowM1').val();			// get value for row dimension
		var numCols = $('#colM1').val();			// get value for column dimension
		var clearElem = $('#inputsM1').empty();		// clear the input elements, so that new dimensions can be set
		
		var table1 = $('<table></table>').attr({ id: "matrix1" }); // create empty table with id
		
		
		for (var r = 0; r < numRows; r++) {
			
			var row = $('<tr>').appendTo(table1);	// create a row and add it to the table
			
			for (var c = 0; c < numCols; c++) {
			var col = $('<td>').appendTo(row);		// create a column and add it to the row
			var input = $('<input type="text" name="inM1_'+r+'[]" size="5"/>').appendTo(col); // create input element and add it to the column element
			$('</td>').appendTo(row);				// end the column element and add it to the row element (ex: <tr><td></td>)
			}
			$('</tr>').appendTo(row);				// end the row element and add it to the row element, so that the page has the following: <tr><td></td>...</tr>
		}
		
		table1.appendTo("#inputsM1");				// When finished creating table with input elements, add table to the division element
	}); // end of setDim1 function
	
	
	// Function for creating Matrix 2 input elements, operates the same
	// as the function for Matrix 1
	$('#setDim2').click(function() {
		
		var numRows = $('#rowM2').val();
		var numCols = $('#colM2').val();
		var clearElem = $('#inputsM2').empty();
		
		var table2 = $('<table></table>').attr({ id: "matrix2" });
		
		for (var r = 0; r < numRows; r++) {
			
			var row = $('<tr>').appendTo(table2);
			
			for (var c = 0; c < numCols; c++) {
				var col = $('<td>').appendTo(row);
				var input = $('<input type="text" name="inM2_'+r+'[]" size="5"/>').appendTo(col);
				$('</td>').appendTo(row);
			}
			$('</tr>').appendTo(row);
		}
		
		table2.appendTo("#inputsM2");
		
	});

	
	
	/*** event handler for returning response from server to webpage ***/
	$('#formData').on('submit', function(e) {
		
		e.preventDefault();	// prevent html page from redirecting or refreshing
		
		$.ajax({									// AJAX request
				type: 'POST',						// Indicates "POST" request
				url: 'run_python.php',				// URL to send the request to
				data: $('#formData').serialize(),	// Data to be sent to the server
				
				success: function(response) {		// Function to be called if the request succeeds
					$('#serverData').html(response); // Return the response from server to html element
													 // with id "#serverData"
				}
				
		});
	
		
	});
		
	
});