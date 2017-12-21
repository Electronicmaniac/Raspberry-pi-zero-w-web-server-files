<html>
<body>
<?php
ini_set('display_errors', 1);

$username="root";
$password="Mobility";
$database="Windturbine_database";

$con = mysqli_connect("localhost", $username, $password, $database);

$query="SELECT*FROM WindturbineLog";
$result=mysqli_query($con, $query);

$num=mysqli_num_rows($result);

$voltageValues = array();

$i=0;
while ($i < $num)
{
	$dateAndValues = array();
	$row = mysqli_fetch_row($result);

	//$dateAndValues["Date & time"] = $row[0]; vorige versie
	$datetime = $row[0];

	//$dateAndValues["Voltage"] = $row[1]; vorige versie
	$voltage = $row[1];

	//$dateAndValues["Current"] = $row[2]; vorige versie
	$current = $row[2];

	//$voltageValues[$i]=$dateAndValues; vorige versie

	/*echo "<table border="1">";
	echo "<tr>";
	echo "<td></td>";
	echo "</tr>";
	echo "</table>";*/
	$i++;
}

//echo json_encode($voltageValues); vorige versie

?>
<table border="1">

<tr>
<th>Datetime</th>
<th>Voltage</th>
<th>Current</th>
</tr>

<tr>
<td><?php echo $datetime; ?></td>
<td><?php echo $voltage; ?></td>
<td><?php echo $current; ?></td>
</tr>

</table>
</body>
</html>
