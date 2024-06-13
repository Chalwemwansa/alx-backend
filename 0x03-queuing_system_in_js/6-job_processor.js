// creates a queue that listens for new jobs and if the jobs are done executing
const kue = require('kue');
const redis = require('redis');

function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}\n`);
};

const push_notification_code = kue.createQueue({
  redis: {
    createClientFactory: () => redis.createClient(),
  },
});

push_notification_code.on('job enqueue', (id, type) => {
  kue.Job.get(id, (err, job) => {
    if (err) {
      console.log(`error: ${err}`);
    } else {
      sendNotification(job.data.phoneNumber, job.data.message);
    };
  });
});
