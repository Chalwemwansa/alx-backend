// module contains a redis client created to handle redis commands
const redis = require('redis');

const client = redis.createClient()
  .on('error', (err) => {
    console.log(`error: ${err}`);
  })
  .on('connect', () => {
    console.log(`successfully connected to the server`);
  });

client.hset('HolbertonSchools', 'Portland', 50, redis.print);
client.hset('HolbertonSchools', 'Seattle', 80, redis.print);
client.hset('HolbertonSchools', 'New York', 20, redis.print);
client.hset('HolbertonSchools', 'Bogota', 20, redis.print);
client.hset('HolbertonSchools', 'Cali', 40, redis.print);
client.hset('HolbertonSchools', 'Paris', 2, redis.print);
client.hgetall('HolbertonSchools', (err, reply) => {
  if (err) {
    console.log(`error: ${err}`);
  } else {
    console.log(reply);
  };
});
