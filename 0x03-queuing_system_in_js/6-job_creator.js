// this module contains code that shows how to use kue to make a push_notification_code
// and process data in the queue while using redis as the client
const kue = require('kue');
const redis = require('redis');

const push_notification_code = kue.createQueue({
  redis: {
    createClientFactory: () => redis.createClient(),
  },
});

push_notification_code.on('job enqueue', (id, type) => {
  console.log(`Notification job created: ${id}`);
});

push_notification_code.on('job complete', (id, result) => {
  console.log('Notification job completed');
});

const data = {
  phoneNumber: '+260974627453',
  message: 'this is chalwes personal line',
};

const job1 = push_notification_code.createJob('myJob', data);
job1.save((err) => {
  if (err) {
    console.log('Notification job failed');
  };
});
