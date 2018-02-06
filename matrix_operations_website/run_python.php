<?php 

// Turn on PHP error reporting
 ini_set('display_errors', 'On');
 error_reporting(E_ALL | E_STRICT);
 	
 	// Check for "POST" request
	if ($_SERVER["REQUEST_METHOD"] == "POST") {
		
		// stop executing script and display appropriate error message if operation was not selected
		if ($_POST['op'] == "choose matrix") {
			die("Did not select matrix operation");
		}
		// stop executing script if any matrix dimensions were not entered and check for blank spaces
		if (!isset($_POST['M1dimRow']) | trim($_POST['M1dimRow']) == '') {
			die("Did not enter row number for Matrix 1");
		}
		if (!isset($_POST['M1dimCol']) | trim($_POST['M1dimCol']) == '') {
			die("Did not enter column number for Matrix 1");
		}
		if (!isset($_POST['M2dimRow']) | trim($_POST['M2dimRow']) == '') {
			die("Did not enter row number for Matrix 2");
		}
		if (!isset($_POST['M2dimCol']) | trim($_POST['M2dimCol']) == '') {
			die("Did not enter column number for Matrix 2");
		}
		
		$op = $_POST['op'];				// name for the matrix operation
						
		$m1Row = $_POST['M1dimRow'];	// matrix 1 row dimension
		$m1Row = (int)$m1Row;			// convert row dimension from string to integer

		$m1Col = $_POST['M1dimCol']; 	// matrix 1 column dimension
		$m1Col = (int)$m1Col;			// convert column dimension from string to integer

		$m2Row = $_POST['M2dimRow'];	// matrix 2 row dimension
		$m2Row = (int)$m2Row;			// convert row dimension from string to integer

		$m2Col = $_POST['M2dimCol']; 	// matrix 2 column dimension
		$m2Col = (int)$m2Col;			// convert column dimension from string to integer

	


		$matrix_1 = array();	// create array for matrix 1
		$matrix_2 = array();	// create array for matrix 2
	
	
		$inc = 0;								
	
		for($i=1; $i <= $m1Row; $i++) {			// loop through each row of matrix 1

		$m1_rows = $_POST['inM1_'.$inc.''];		// post each row of matrix 1 as an array
		$arrToString = implode(",", $m1_rows); 	// convert each row from an array to a string
	
		//$matrix_1[] = explode(',', $arrToString); 
		$matrix_1[] = array_map('intval', explode(',', $arrToString));		// convert the string to an array of integer values
		$inc++;									// Changes the name attribute of the input element array
												// for each row of matrix 1

		}


 		$inc = 0;
		for($i=1; $i <= $m2Row; $i++) { 		// loop through each row of matrix 2
  
  		$m2_rows = $_POST['inM2_'.$inc.''];		// post each row of matrix 2 as an array
  		$arrToString = implode(",", $m2_rows);	// convert each row from an array to a string
	
		//$matrix_2[] = explode(',', $arrToString);	
		$matrix_2[] = array_map('intval', explode(',', $arrToString));		// convert the string to an array of integer values
  		$inc++;									// Changes the name attribute of the input element array
												// for each row of matrix 2
  		}

 	

		$json1 = json_encode($matrix_1);		// encodes array to json format for matrix 1
	
		$json2 = json_encode($matrix_2);		// encodes array to json format for matrix 2

/*
	if (file_put_contents("matrix_1_data.json", $json1) && file_put_contents("matrix_2_data.json", $json2)) {			// create json file and write the string of matrix 1 in json file
		
			
		echo "<br><br>Both JSON files created succesfully";		// indicate if both JSON files were created
	}
	
	else {
		echo "<br>Error creating JSON file";			// indicate if there was an error creating the file
		}
*/  
	 	// pass variables to python script
	 	$command = 'python matrix_ops.py ' . $m1Col . ' ' . $m2Row . ' ' . $op . ' ' . $m1Row . ' ' . 
	 									$m2Col . ' ' . $json1 . ' ' . $json2;
	 	echo "<br>";
	 	//
	 	// Function: passthru
	 	// Description: Executes python script with command
	 	// Input: String with path to the python executable and name of python script,
	 	// dimensions for matrix 1 and matrix 2 arrays, array for matrix 1 and array for matrix 2
	 	// Output: Returns the results from the python script
	 	//
	 	passthru($command);
	 
	 
	 
	 

	}


?>