// this node script connects to the redis server
// and logs info to standard output showing that the server is running
// and logs other infor to show that an error occured
import { createClient } from 'redis';

const client = createClient()
  .on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}\n`);
  })
  .on('connect', () => {
    console.log('Redis client connected to the server\n');
  });
