<?php

$base_url = 'https://www.xxx.xx/api/v2/org/';
$api_key = 'xxx';
$secret_key = 'xxx';
$http_header = array('X-ACCESS-KEY:' . $api_key, 'User-Agent:wallex-P 1.0');

function post_data($url = '', $post_data = array())
{
    $curl = curl_init();
    curl_setopt($curl, CURLOPT_URL, $GLOBALS['base_url'] . $url);
    curl_setopt($curl, CURLOPT_TIMEOUT, 20);
    curl_setopt($curl, CURLOPT_POST, 1);
    $post_data['signature'] = sign($post_data);

    curl_setopt($curl, CURLOPT_HTTPHEADER, $GLOBALS['http_header']);
    curl_setopt($curl, CURLOPT_POSTFIELDS, http_build_query($post_data));
    curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);
    $result = curl_exec($curl);
    curl_close($curl);
    return json_decode($result, true);
}

function sign($post_data = array())
{
    ksort($post_data);
    $original_str = http_build_query($post_data);
    return hash_hmac('sha256', $original_str, $GLOBALS['secret_key']);
}

function server_time()
{
    $url = 'basic/time';
    $data = post_data($url);
    var_dump($data);
}

function user_info($user_id)
{
    $post_data['user_id'] = $user_id;
    $url = 'user/get_base_info';
    $data = post_data($url, $post_data);
    var_dump($data);
}

function query_user_list($from_id = 0, $start_time = 0, $end_time = 0, $limit = 20)
{
    $post_data['from_id'] = $from_id;
    $post_data['start_time'] = $start_time;
    $post_data['end_time'] = $end_time;
    $post_data['limit'] = $limit;
    $url = 'user/query_user_list';
    $data = post_data($url, $post_data);
    var_dump($data);
}

// get all balance data
function token_hold_detail($token_id, $from_id = 0, $limit = 100, $index = 0)
{
    $post_data['token_id'] = $token_id;
    $post_data['from_id'] = $from_id;
    $post_data['limit'] = $limit;
    $url = 'statistics/token_hold_detail';
    var_dump($post_data);
    $data = post_data($url, $post_data);
    var_dump($data);
    // echo '--------';
    // echo 'index:' . strval($index) . ' data size is ' . strval(count($data['data'])) . ' and lastid is ' . strval($data['data'][9]['id']);
    // echo " --------\n";
    // if (count($data['data']) == $limit) {
    //     token_hold_detail($token_id, $data['data'][$limit - 1]['id'], $limit, $index + 1);
    // }
}

function org_trade_detail($symbol_id = '', $from_id = 0, $start_time = 0, $end_time = 0, $limit = 10, $index = 0)
{
    $post_data['symbol_id'] = $symbol_id;
    $post_data['from_id'] = $from_id;
    $post_data['start_time'] = $start_time;
    $post_data['end_time'] = $end_time;
    $post_data['limit'] = $limit;
    $url = 'statistics/trade_detail';
    $data = post_data($url, $post_data);
    var_dump($data);

    // echo '--------';
    // echo 'index:' . strval($index) . ' data size is ' . strval(count($data['data'])) . ' and lastid is ' . strval($data['data'][9]['tradeId']);
    // echo " --------\n";
    // if (count($data['data']) == $limit) {
    //     org_trade_detail($symbol_id, $data['data'][$limit - 1]['tradeId'], $limit, $index + 1);
    // }
}

server_time();

// user_info(97298429944266752);
// org_trade_detail();
