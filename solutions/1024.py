import sys
class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        clips = sorted(clips, key=lambda x: (x[0] * 100000) - x[1])
        print(clips)
        cur_length = 0
        num = 0
        highest = 0
        while len(clips) > 0 and highest < T:
            cur, clips = clips[0], clips[1:]
            if cur_length >= cur[1]:
                continue
            if cur_length < cur[0] and highest < cur[0]:
                return -1
            if cur_length < cur[0]:
                cur_length = highest
                num +=1
                print(cur)
                highest = -1
            
            highest = max(cur[1], highest)
            print(highest, cur_length, cur[0])
        if cur_length < T:
            cur_length = highest
            num +=1
            
        if cur_length < T:
            return -1
        else:
            return num
