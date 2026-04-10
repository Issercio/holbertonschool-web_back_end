# Redis Installation and Setup for Queuing System in JS

## Task 0: Install a Redis Instance

Follow these steps to install and run Redis 6.0.10, set a key, and prepare your project:

### 1. Download and Extract Redis
```
wget http://download.redis.io/releases/redis-6.0.10.tar.gz
tar xzf redis-6.0.10.tar.gz
cd redis-6.0.10
```

### 2. Compile Redis
```
make
```

### 3. Start Redis in the Background
```
src/redis-server &
```

### 4. Test Redis Server
```
src/redis-cli ping
# Should return: PONG
```

### 5. Set and Get a Key
```
src/redis-cli set Holberton School
# Should return: OK
src/redis-cli get Holberton
# Should return: "School"
```

### 6. Stop the Redis Server
Find the process ID and kill it:
```
ps aux | grep redis-server
kill [PID_OF_Redis_Server]
```

### 7. Copy the dump.rdb File
Copy the generated `dump.rdb` file into the root of the `queuing_system_in_js` project directory.

---

## Verification
- Running `get Holberton` in the Redis client should return `School`.

---

## Files
- `README.md` (this file)
- `dump.rdb` (should be present in the root of `queuing_system_in_js`)
