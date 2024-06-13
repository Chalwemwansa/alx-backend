// module contains numbers to be blacklisted and shows how to track
// jobs using kue
const kue = require('kue');
const redis = require('redis');

const blacklist = ['4153518780', '4153518781'];

function sendNotification(phoneNumber, message, job, done) {
  job.progress(0, 100);
  if (blacklist.includes(phoneNumber)) {
    const err = new Error(`Phone number ${phoneNumber} is blacklisted`);
    return done(err);
  } else {
    job.progress(50, 100);
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    return done(null, 'done');
  };
};

const queue = kue.createQueue({
  redis: {
    createClientFactory: () => redis.createClient(),
  },
});

queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});
