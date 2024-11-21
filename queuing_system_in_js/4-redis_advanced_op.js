import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to server: ${err}`);
});

function createHash() {
  const hashKey = 'HolbertonSchools';

  // Delete the hash before creating it to avoid getting Reply: 0
  client.del(hashKey, (delError, delReply) => {
    if (delError) {
      console.error(`Error deleting hash: ${delError}`);
    } else {
      console.log(`Deleted hash: ${delReply}`);
    }

    // After the hash is deleted, set the values
    client.hset(hashKey, 'Portland', 50, redis.print);
    client.hset(hashKey, 'Seattle', 80, redis.print);
    client.hset(hashKey, 'New York', 20, redis.print);
    client.hset(hashKey, 'Bogota', 20, redis.print);
    client.hset(hashKey, 'Cali', 40, redis.print);
    client.hset(hashKey, 'Paris', 2, redis.print);

    displayHash(hashKey);
  });
}

// Display the Hash using hgetall
function displayHash(hashKey) {
  client.hgetall(hashKey, (error, object) => {
    if (error) {
      console.error('Error retrieving hash:', error);
    } else {
      console.log(object);
    }
  });
}

// Call the functions
createHash();
