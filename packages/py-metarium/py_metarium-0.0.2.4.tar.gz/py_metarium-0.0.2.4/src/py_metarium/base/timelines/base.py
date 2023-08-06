class TimeLine(object):

    TIMELINE_RECONNECTION_WAIT_DURATION_SECONDS = 5
    MAX_TIMELINE_RECONNECTION_ATTEMPTS = 10
    POINT_PREFIX = "time"

    def prefix(self):
        raise NotImplementedError
    
    def info(self):
        raise NotImplementedError
    
    def get_points(self):
        raise NotImplementedError
    
    def get_block_hash_from_block_number(self, block_number):
        raise NotImplementedError
    
    def get_tip_number(self, finalized_only=False):
        raise NotImplementedError
