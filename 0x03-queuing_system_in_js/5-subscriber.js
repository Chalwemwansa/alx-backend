// module contains code that has redis subscribing to a channel then
// longging the infor passed as a message to the channel
const redis = require('redis');

const client = redis.createClient()
  .on('error', (err) => {
    console.log(`redis client not connected to the server: ${err}`);
  })
  .on('connect', () => {
    console.log('Redis client connected to the server');
  });

client.subscribe('holberton school channel');

client.on('message', (channel, msg) => {
  console.log(msg);
  if (msg === 'KILL_SERVER') {
    client.unsubscribe();
    client.quit();
  };
});
