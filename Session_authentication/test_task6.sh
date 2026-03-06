#!/bin/bash
# Test script for Task 6

cd /root/holbertonschool-web_back_end/Session_authentication

# Clean up
rm -f .db_User.json

# Start the server in background and capture output
API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth SESSION_NAME=_my_session_id ./main_4.py > /tmp/server_output.txt 2>&1 &
SERVER_PID=$!

# Wait for server to start
sleep 3

# Extract session ID from output
SESSION_ID=$(grep "Session ID:" /tmp/server_output.txt | awk '{print $NF}')
echo "Session ID captured: $SESSION_ID"
echo ""

# Run tests
echo "Test 1: No cookie"
curl "http://0.0.0.0:5000/"
echo ""

echo "Test 2: Invalid cookie"
curl "http://0.0.0.0:5000/" --cookie "_my_session_id=Holberton"
echo ""

echo "Test 3: Valid cookie with session ID"
curl "http://0.0.0.0:5000/" --cookie "_my_session_id=$SESSION_ID"
echo ""

# Clean up
kill $SERVER_PID 2>/dev/null
