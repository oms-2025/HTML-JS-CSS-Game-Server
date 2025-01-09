<?php
session_start();

$username = $_POST['username'];
$password = $_POST['password'];

$admins = json_decode(file_get_contents('admin.json'), true);

foreach ($admins as $admin) {
    if ($admin['username'] === $username && password_verify($password, $admin['password'])) {
        $_SESSION['admin_loggedin'] = true;
        header('Location: server.html');
        exit();
    }
}

header('Location: server.html?error=invalid_credentials');
exit();
?>