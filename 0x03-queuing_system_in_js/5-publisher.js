// this module coontains a functionthen another channel reads from the channel
const redis = require('redis');

const client = redis.createClient()
  .on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
  })
  .on('connect', () => {
    console.log('Redis client connected to the server');
  });

function publishMessage(message, time) {
  setTimeout(() => {
    console.log(`About to send ${message}`);
    client.publish('holberton school channel', message, (err) => {
      if (err) {
        console.log(err);
      };
    });
  }, time)
};

publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);

