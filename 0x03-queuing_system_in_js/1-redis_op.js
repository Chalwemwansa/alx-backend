// this node script connects to the redis server
// and logs info to standard output showing that the server is running
// and logs other infor to show that an error occured
const redis = require('redis');
import { createClient } from 'redis';

const client = createClient()
  .on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}\n`);
  })
  .on('connect', () => {
    console.log('Redis client connected to the server\n');
  });

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
};

function displaySchoolValue(schoolName) {
  client.get(schoolName, (error, reply) => {
    if (error) {
      console.log(`error occured: ${error}\n`);
    } else {
      console.log(reply);
    };
  });
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
