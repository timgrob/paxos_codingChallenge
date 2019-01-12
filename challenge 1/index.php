<?php

$connection = mysqli_connect('timgrob1.mysql.db.internal', 'timgrob1_admin', 'admin', 'timgrob1_paxos');
$request_method = $_SERVER["REQUEST_METHOD"];

function get_message($message_sha256) {
    global $connection;
    $query = "SELECT * FROM posts WHERE sha='{$message_sha256}'";
    $result = mysqli_query($connection, $query);
    $rowResult = mysqli_fetch_array($result, MYSQLI_NUM);

    if(!empty($rowResult)) {
        $response=array(
            'status' => 200,
            'message' => $rowResult[2]
        );
    }
    else {
        $response=array(
            'status' => 404,
            'err_msg' =>'Message not found'
        );
    }

    header('Content-Type: application/json');
    echo json_encode($response);
}

function post_message($message_plain) {
    global $connection;
    $sha256 = hash('sha256', $message_plain);
    $query="INSERT INTO posts SET message='{$message_plain}', sha='{$sha256}'";

    if(mysqli_query($connection, $query))
    {
        $response=array(
            'status' => 201,
            'digest' => $sha256
        );
    }
    else {
        $response=array(
            'status' => 500,
            'status_message' =>'Something went wrong.'
        );
    }
    header('Content-Type: application/json');
    echo json_encode($response);

}

switch ($request_method) {
    case 'GET':
        if (isset($_GET['sha'])) {
            get_message($_GET['sha']);
        } else {
            $response=array(
                'status' => 204,
                'message' =>'No sha256 code given.'
            );
            header('Content-Type: application/json');
            echo json_encode($response);
        }
        break;
    case 'POST':
        $message = $_POST["message"];
        post_message($message);
        break;
    default:
        header("HTTP/1.0 405 Method Not Allowed");
        break;
}