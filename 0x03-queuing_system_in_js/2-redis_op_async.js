// this node script connects to the redis server
// and logs info to standard output showing that the server is running
// and logs other infor to show that an error occured
const redis = require('redis');
const { promisify } = require('util');

const client = redis.createClient()
  .on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}\n`);
  })
  .on('connect', () => {
    console.log('Redis client connected to the server\n');
  });

// make the promisified objects using promisify to be able to use async
const asyncSet =  promisify(client.set).bind(client);
const asyncGet = promisify(client.get).bind(client);

async function setNewSchool(schoolName, value) {
  try {
    await asyncSet(schoolName, value);
    console.log(`Reply: OK`);
  } catch (err) {
    console.log(`error: ${err}\n`);
  };
};

async function displaySchoolValue(schoolName) {
  try {
    const reply = await asyncGet(schoolName);
    if (reply) {
      console.log(reply);
    };
  } catch (err) {
    console.log(`error: ${err}\n`);
  };
};


(async () => {
  await displaySchoolValue('Holberton');
  await setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
})();
