<?php
// Start the session
session_start();

// Check if the username is stored in the session
if (isset($_SESSION['nickname'])) {
 file_put_contents('log.txt', $_SESSION['uname'] . "ssss\n", FILE_APPEND);
  echo $_SESSION['nickname'];
} else {
  // Return an error message if the username is not set in the session
  echo 'Error: username not set in the session.';
}
?>