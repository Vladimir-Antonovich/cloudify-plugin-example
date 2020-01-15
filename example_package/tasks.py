from cloudify import ctx
from cloudify.state import ctx_parameters as inputs
from datetime import datetime, timedelta
from time import sleep
from cloudify.decorators import operation


@operation
def write_to_file(*args, **kwargs):
    with open('/tmp/cloudify-plugin', 'w') as f:
        f.write('This simple example gives you the power to do amazing things.\n')

@operation(resumable=True)
def tick(ctx, **kwargs):
    test_time = int(inputs.get('test_time', 30))
    end_time = datetime.now() + timedelta(0,test_time)
    while True:
        ctx.logger.info("test_func: {}".format(datetime.now()))
        if datetime.now() >= end_time:
            return
        sleep(1)
