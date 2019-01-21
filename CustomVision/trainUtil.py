#Split video to frames

import cv2
import os

bg_type = "hack\\"
base_home_url = "C:\\Users\\91987\\Documents\\Oxford\\HackCambridge\\" + bg_type
base_vid_url = "C:\\Users\\91987\\Documents\\Oxford\\HackCambridge\\"+bg_type+"Videos\\"
base_frm_url = "C:\\Users\\91987\\Documents\\Oxford\\HackCambridge\\"+bg_type+"frames\\"

for i in range(1,4):
    vid_name = "Demo2-"+str(i)
    vidcap = cv2.VideoCapture(base_vid_url + vid_name + ".mov")
    success,image = vidcap.read()
    count = 0
    print(success)
    while success:
        if not os.path.exists(base_frm_url + vid_name):
            os.makedirs(base_frm_url + vid_name)

        cv2.imwrite(base_frm_url + vid_name + "\\frame" + str(count) + ".jpg", image)
        success,image = vidcap.read()
        count += 1

# To create videos with bounded boxes
import cv2,re,os
from os.path import isfile, join
 
def convert_frames_to_video(pathIn,pathOut,fps):
    frame_array = []
    files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
 
    #for sorting the file names properly
    files.sort(key = lambda x: int(x[5:-4]))
 
    for i in range(len(files)):
        filename=pathIn + files[i]
        #reading each files
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height)
        print(filename)
        #inserting the frames into an image array
        frame_array.append(img)
 
    out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
 
    for i in range(len(frame_array)):
        # writing to a image array
        out.write(frame_array[i])
    out.release()
    
from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateEntry, Region

base_home_url = "C:\\Users\\91987\\Documents\\Oxford\\HackCambridge\\Home_01\\Home_01\\"
base_vid_url = base_home_url + "Videos\\"
base_frm_url = base_home_url + "frames\\video (2)\\"
bounded_frm_url = base_home_url + "frames\\video (2)_bounded\\"


with open(base_home_url + "Annotation_files\\video (2).txt") as f:
    start_frame = [int(x) for x in next(f).split()] # read first line
    end_frame = [int(x) for x in next(f).split()] # read second line
    array = []
    for line in f: # read rest of lines
        array.append([int(x) for x in line.split(',')])

start_frame = start_frame[0]
end_frame = end_frame[0]

for frm_num in range(len(array)):
    cur = array[frm_num]
    h = float(cur[4])
    w = float(cur[5])
    cx = float(cur[2])
    cy = float(cur[3])
    print(cur)
    if frm_num <start_frame:
        img = cv2.imread(base_frm_url + "frame" + str(frm_num) + ".jpg")
        cv2.rectangle(img,(int(cx-w/4),int(cy-h/4)),(int(cx+w/2),int(cy+h/2)),(255,255,255),1)
        cv2.imwrite( bounded_frm_url + "frame" + str(frm_num) + ".jpg", img );
    elif frm_num <= end_frame:
        img = cv2.imread(base_frm_url + "frame" + str(frm_num) + ".jpg")
        cv2.rectangle(img,(int(cx),int(cy)),(int(cx+w/2),int(cy+h/2)),(0,255,255),1)
        cv2.imwrite( bounded_frm_url + "frame" + str(frm_num) + ".jpg", img );
    elif frm_num <= 225:
        img = cv2.imread(base_frm_url + "frame" + str(frm_num) + ".jpg")
        cv2.rectangle(img,(int(cx),int(cy)),(int(cx+w/2),int(cy+h/2)),(0,0,255),1)    
        cv2.imwrite( bounded_frm_url + "frame" + str(frm_num) + ".jpg", img );
    frm_num = frm_num + 1

            
pathOut = 'video.avi'
fps = 25.0
convert_frames_to_video(bounded_frm_url, 'video (2)_bounded.avi', fps)

## Setup Custom Vision Project and initiate project

from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateEntry, Region

base_home_url = "C:\\Users\\91987\\Documents\\Oxford\\HackCambridge\\Home_01\\Home_01\\"
base_vid_url = base_home_url + "Videos\\"
base_frm_url = base_home_url + "frames\\"

ENDPOINT = "https://southcentralus.api.cognitive.microsoft.com"

# Replace with a valid key
training_key = "d4b847b33764429f959d992812107f05"
prediction_key = "fdc8548027114381bd41337662282bc5"

trainer = CustomVisionTrainingClient(training_key, endpoint=ENDPOINT)

# Find the object detection domain
obj_detection_domain = next(domain for domain in trainer.get_domains() if domain.type == "ObjectDetection")

# Create a new project
print ("Creating project...")
project = trainer.create_project("Human Detection", domain_id=obj_detection_domain.id)

# Make two tags in the new project
# human_tag = trainer.create_tag(project.id, "human")
standing_tag = trainer.create_tag(project.id, "standing")
falling_tag = trainer.create_tag(project.id, "falling")
fallen_tag = trainer.create_tag(project.id, "fallen")


standing_image_regions = {
1:[0.4890625,0.463802083,0.640625,0.291666667],
2:[0.4890625,0.463802083,0.640625,0.291666667],
3:[0.4890625,0.463802083,0.640625,0.291666667],
4:[0.4890625,0.463802083,0.640625,0.291666667],
5:[0.4890625,0.463802083,0.640625,0.291666667],
6:[0.4890625,0.463802083,0.640625,0.291666667],
7:[0.4890625,0.463802083,0.640625,0.291666667],
8:[0.4890625,0.463802083,0.640625,0.291666667],
9:[0.4890625,0.463802083,0.640625,0.291666667],
10:[0.4890625,0.463802083,0.640625,0.291666667],
11:[0.4890625,0.463802083,0.640625,0.291666667],
12:[0.4890625,0.463802083,0.640625,0.291666667],
13:[0.4890625,0.463802083,0.640625,0.291666667],
14:[0.4890625,0.463802083,0.640625,0.291666667],
15:[0.4890625,0.463802083,0.640625,0.291666667],
16:[0.4890625,0.463802083,0.640625,0.291666667],
17:[0.4890625,0.463802083,0.640625,0.291666667],
18:[0.4890625,0.463802083,0.640625,0.291666667],
19:[0.4890625,0.463802083,0.640625,0.291666667],
20:[0.4890625,0.463802083,0.640625,0.291666667],
21:[0.4890625,0.463802083,0.640625,0.291666667],
22:[0.4890625,0.463802083,0.640625,0.291666667],
23:[0.4890625,0.463802083,0.640625,0.291666667],
24:[0.4890625,0.463802083,0.640625,0.291666667],
25:[0.4890625,0.463802083,0.640625,0.291666667],
26:[0.4890625,0.463802083,0.640625,0.291666667],
27:[0.4890625,0.463802083,0.640625,0.291666667],
28:[0.4890625,0.463802083,0.640625,0.291666667],
29:[0.4890625,0.463802083,0.640625,0.291666667],
30:[0.4890625,0.463802083,0.640625,0.291666667],
31:[0.4890625,0.463802083,0.640625,0.291666667],
32:[0.4890625,0.463802083,0.640625,0.291666667],
33:[0.4890625,0.463802083,0.640625,0.291666667],
34:[0.4890625,0.463802083,0.640625,0.291666667],
35:[0.4890625,0.463802083,0.640625,0.291666667],
36:[0.4890625,0.463802083,0.640625,0.291666667],
37:[0.4890625,0.463802083,0.640625,0.291666667],
38:[0.4890625,0.463802083,0.640625,0.291666667],
39:[0.4890625,0.463802083,0.640625,0.291666667],
40:[0.4890625,0.463802083,0.640625,0.291666667],
41:[0.4890625,0.463802083,0.640625,0.291666667],
42:[0.4890625,0.463802083,0.640625,0.291666667],
43:[0.4890625,0.463802083,0.640625,0.291666667],
44:[0.4890625,0.463802083,0.640625,0.291666667],
45:[0.4890625,0.463802083,0.640625,0.291666667],
46:[0.5140625,0.426302083,0.646875,0.308333333],
47:[0.5140625,0.426302083,0.646875,0.308333333],
48:[0.5140625,0.426302083,0.646875,0.308333333],
49:[0.5140625,0.426302083,0.646875,0.308333333],
50:[0.5140625,0.426302083,0.646875,0.308333333],
51:[0.5140625,0.426302083,0.646875,0.308333333],
52:[0.5140625,0.426302083,0.646875,0.308333333],
53:[0.528125,0.415104167,0.64375,0.329166667],
54:[0.528125,0.415104167,0.64375,0.329166667],
55:[0.528125,0.415104167,0.64375,0.329166667],
56:[0.528125,0.415104167,0.64375,0.329166667],
57:[0.528125,0.415104167,0.64375,0.329166667],
58:[0.528125,0.415104167,0.64375,0.329166667],
59:[0.528125,0.415104167,0.64375,0.329166667],
60:[0.528125,0.415104167,0.64375,0.329166667],
61:[0.528125,0.415104167,0.64375,0.329166667],
62:[0.528125,0.415104167,0.64375,0.329166667],
63:[0.528125,0.415104167,0.64375,0.329166667],
64:[0.528125,0.415104167,0.64375,0.329166667],
65:[0.528125,0.415104167,0.64375,0.329166667],
66:[0.528125,0.415104167,0.64375,0.329166667],
67:[0.528125,0.415104167,0.64375,0.329166667],
68:[0.540625,0.4296875,0.61875,0.308333333],
69:[0.540625,0.4296875,0.61875,0.308333333],
70:[0.540625,0.4296875,0.61875,0.308333333],
71:[0.540625,0.4296875,0.61875,0.308333333],
72:[0.540625,0.4296875,0.61875,0.308333333],
73:[0.5046875,0.46015625,0.653125,0.3375],
74:[0.5046875,0.46015625,0.653125,0.3375],
75:[0.5046875,0.46015625,0.653125,0.3375],
76:[0.5046875,0.46015625,0.653125,0.3375],
77:[0.5046875,0.46015625,0.653125,0.3375],
78:[0.5046875,0.46015625,0.653125,0.3375],
79:[0.5046875,0.46015625,0.653125,0.3375],
80:[0.5046875,0.46015625,0.653125,0.3375],
81:[0.5046875,0.46015625,0.653125,0.3375],
82:[0.5046875,0.46015625,0.653125,0.3375],
83:[0.5046875,0.46015625,0.653125,0.3375],
84:[0.5046875,0.46015625,0.653125,0.3375],
85:[0.5046875,0.46015625,0.653125,0.3375],
86:[0.525,0.4125,0.65,0.2625],
87:[0.525,0.4125,0.65,0.2625],
88:[0.525,0.4125,0.65,0.2625],
89:[0.5046875,0.426822917,0.653125,0.245833333],
90:[0.5046875,0.426822917,0.653125,0.245833333],
91:[0.5046875,0.426822917,0.653125,0.245833333],
92:[0.5046875,0.426822917,0.653125,0.245833333],
93:[0.5046875,0.426822917,0.653125,0.245833333],
94:[0.5046875,0.426822917,0.653125,0.245833333],
95:[0.5046875,0.426822917,0.653125,0.245833333],
96:[0.509375,0.4453125,0.6375,0.204166667],
97:[0.509375,0.4453125,0.6375,0.204166667],
98:[0.509375,0.4453125,0.6375,0.204166667],
99:[0.509375,0.4453125,0.6375,0.204166667],
100:[0.509375,0.4453125,0.6375,0.204166667],
101:[0.4890625,0.438802083,0.653125,0.179166667],
102:[0.4890625,0.438802083,0.653125,0.179166667],
103:[0.4890625,0.438802083,0.653125,0.179166667],
104:[0.4890625,0.438802083,0.653125,0.179166667],
105:[0.4890625,0.438802083,0.653125,0.179166667],
106:[0.4890625,0.438802083,0.653125,0.179166667],
107:[0.4890625,0.438802083,0.653125,0.179166667],
108:[0.4921875,0.399739583,0.609375,0.1625],
109:[0.4921875,0.399739583,0.609375,0.1625],
110:[0.4921875,0.399739583,0.609375,0.1625],
111:[0.4921875,0.399739583,0.609375,0.1625],
112:[0.4921875,0.399739583,0.609375,0.1625],
113:[0.4828125,0.454427083,0.596875,0.1625],
114:[0.4828125,0.454427083,0.596875,0.1625],
115:[0.4828125,0.454427083,0.596875,0.1625],
116:[0.4640625,0.463802083,0.596875,0.166666667],
117:[0.4640625,0.463802083,0.596875,0.166666667],
118:[0.4640625,0.463802083,0.596875,0.166666667],
119:[0.4640625,0.463802083,0.596875,0.166666667],
120:[0.4515625,0.49921875,0.596875,0.166666667],
121:[0.4515625,0.49921875,0.596875,0.166666667],
122:[0.4515625,0.49921875,0.596875,0.166666667],
123:[0.4421875,0.57890625,0.584375,0.158333333],
124:[0.4421875,0.57890625,0.584375,0.158333333],
125:[0.4421875,0.57890625,0.584375,0.158333333],
126:[0.4421875,0.57890625,0.584375,0.158333333],
127:[0.421875,0.605729167,0.56875,0.158333333],
128:[0.421875,0.605729167,0.56875,0.158333333],
129:[0.421875,0.605729167,0.56875,0.158333333],
130:[0.421875,0.605729167,0.56875,0.158333333],
131:[0.4296875,0.576822917,0.521875,0.179166667],
132:[0.4296875,0.576822917,0.521875,0.179166667],
133:[0.4296875,0.576822917,0.521875,0.179166667],
134:[0.421875,0.584895833,0.53125,0.183333333],
135:[0.421875,0.584895833,0.53125,0.183333333],
136:[0.421875,0.584895833,0.53125,0.183333333],
137:[0.421875,0.584895833,0.53125,0.183333333],
138:[0.4125,0.59375,0.5,0.170833333],
139:[0.4125,0.59375,0.5,0.170833333],
140:[0.4125,0.59375,0.5,0.170833333],
141:[0.403125,0.594270833,0.475,0.216666667],
142:[0.403125,0.594270833,0.475,0.216666667],
143:[0.403125,0.594270833,0.475,0.216666667]
}


falling_image_regions = {
144:[0.384375,0.6078125,0.46875,0.241666667],
145:[0.384375,0.6078125,0.46875,0.241666667],
146:[0.384375,0.6078125,0.46875,0.241666667],
147:[0.3796875,0.614322917,0.434375,0.283333333],
148:[0.3796875,0.614322917,0.434375,0.283333333],
149:[0.3796875,0.614322917,0.434375,0.283333333],
150:[0.396875,0.630729167,0.38125,0.375],
151:[0.390625,0.608854167,0.39375,0.404166667],
152:[0.396875,0.634895833,0.375,0.420833333],
153:[0.396875,0.634895833,0.375,0.420833333],
154:[0.4359375,0.60703125,0.340625,0.470833333],
155:[0.440625,0.600520833,0.3375,0.483333333],
156:[0.4515625,0.607552083,0.334375,0.520833333],
157:[0.4515625,0.607552083,0.334375,0.520833333],
158:[0.4515625,0.607552083,0.334375,0.520833333],
159:[0.4515625,0.607552083,0.334375,0.520833333],
160:[0.4515625,0.607552083,0.334375,0.520833333],
161:[0.509375,0.536979167,0.24375,0.5375],
162:[0.509375,0.536979167,0.24375,0.5375],
163:[0.509375,0.536979167,0.24375,0.5375],
164:[0.525,0.529166667,0.21875,0.5625],
165:[0.525,0.529166667,0.21875,0.5625],
166:[0.525,0.529166667,0.21875,0.5625],
167:[0.5109375,0.53203125,0.240625,0.529166667],
168:[0.5109375,0.53203125,0.240625,0.529166667]
}

fallen_image_regions = {
169:[0.5046875,0.555989583,0.240625,0.5375],
170:[0.5046875,0.555989583,0.240625,0.5375],
171:[0.5046875,0.555989583,0.240625,0.5375],
172:[0.5046875,0.555989583,0.240625,0.5375],
173:[0.5046875,0.555989583,0.240625,0.5375],
174:[0.5046875,0.555989583,0.240625,0.5375],
175:[0.5046875,0.555989583,0.240625,0.5375],
176:[0.5046875,0.555989583,0.240625,0.5375],
177:[0.5046875,0.555989583,0.240625,0.5375],
178:[0.5046875,0.555989583,0.240625,0.5375],
179:[0.5046875,0.555989583,0.240625,0.5375],
180:[0.5046875,0.555989583,0.240625,0.5375],
181:[0.5046875,0.555989583,0.240625,0.5375],
182:[0.5046875,0.555989583,0.240625,0.5375],
183:[0.5046875,0.555989583,0.240625,0.5375],
184:[0.5046875,0.555989583,0.240625,0.5375],
185:[0.5046875,0.555989583,0.240625,0.5375],
186:[0.5046875,0.555989583,0.240625,0.5375],
187:[0.5046875,0.555989583,0.240625,0.5375],
188:[0.5046875,0.555989583,0.240625,0.5375],
189:[0.5046875,0.555989583,0.240625,0.5375],
190:[0.5046875,0.555989583,0.240625,0.5375],
191:[0.5046875,0.555989583,0.240625,0.5375],
192:[0.5046875,0.555989583,0.240625,0.5375],
193:[0.5046875,0.555989583,0.240625,0.5375],
194:[0.5046875,0.555989583,0.240625,0.5375],
195:[0.5046875,0.555989583,0.240625,0.5375],
196:[0.5046875,0.555989583,0.240625,0.5375],
197:[0.5046875,0.555989583,0.240625,0.5375],
198:[0.5046875,0.555989583,0.240625,0.5375],
199:[0.5046875,0.555989583,0.240625,0.5375],
200:[0.5046875,0.555989583,0.240625,0.5375],
201:[0.5046875,0.555989583,0.240625,0.5375],
202:[0.5046875,0.555989583,0.240625,0.5375],
203:[0.5046875,0.555989583,0.240625,0.5375],
204:[0.5046875,0.555989583,0.240625,0.5375],
205:[0.5046875,0.555989583,0.240625,0.5375],
206:[0.5046875,0.555989583,0.240625,0.5375],
207:[0.5046875,0.555989583,0.240625,0.5375],
208:[0.5046875,0.555989583,0.240625,0.5375],
209:[0.5046875,0.555989583,0.240625,0.5375],
210:[0.5046875,0.555989583,0.240625,0.5375],
211:[0.5046875,0.555989583,0.240625,0.5375],
212:[0.5046875,0.555989583,0.240625,0.5375],
213:[0.5046875,0.555989583,0.240625,0.5375],
214:[0.5046875,0.555989583,0.240625,0.5375],
215:[0.5046875,0.555989583,0.240625,0.5375],
216:[0.5046875,0.555989583,0.240625,0.5375],
217:[0.5046875,0.555989583,0.240625,0.5375],
218:[0.5046875,0.555989583,0.240625,0.5375],
219:[0.5046875,0.555989583,0.240625,0.5375],
220:[0.5046875,0.555989583,0.240625,0.5375],
221:[0.5046875,0.555989583,0.240625,0.5375],
222:[0.5046875,0.555989583,0.240625,0.5375],
223:[0.5046875,0.555989583,0.240625,0.5375],
224:[0.5046875,0.555989583,0.240625,0.5375],
225:[0.5046875,0.555989583,0.240625,0.5375],
226:[0.5046875,0.555989583,0.240625,0.5375],
227:[0.5046875,0.555989583,0.240625,0.5375],
228:[0.5046875,0.555989583,0.240625,0.5375],
229:[0.5046875,0.555989583,0.240625,0.5375],
230:[0.5046875,0.555989583,0.240625,0.5375],
231:[0.5046875,0.555989583,0.240625,0.5375],
232:[0.5046875,0.555989583,0.240625,0.5375],
233:[0.5046875,0.555989583,0.240625,0.5375],
234:[0.5046875,0.555989583,0.240625,0.5375],
235:[0.5046875,0.555989583,0.240625,0.5375],
236:[0.5046875,0.555989583,0.240625,0.5375],
237:[0.5046875,0.555989583,0.240625,0.5375],
238:[0.5046875,0.555989583,0.240625,0.5375],
239:[0.5046875,0.555989583,0.240625,0.5375],
240:[0.5046875,0.555989583,0.240625,0.5375],
241:[0.5046875,0.555989583,0.240625,0.5375],
242:[0.5046875,0.555989583,0.240625,0.5375],
243:[0.5046875,0.555989583,0.240625,0.5375],
244:[0.5046875,0.555989583,0.240625,0.5375],
245:[0.5046875,0.555989583,0.240625,0.5375],
246:[0.5046875,0.555989583,0.240625,0.5375],
247:[0.5046875,0.555989583,0.240625,0.5375],
248:[0.5046875,0.555989583,0.240625,0.5375],
249:[0.5046875,0.555989583,0.240625,0.5375],
250:[0.5046875,0.555989583,0.240625,0.5375],
251:[0.5046875,0.555989583,0.240625,0.5375],
252:[0.5046875,0.555989583,0.240625,0.5375],
253:[0.5046875,0.555989583,0.240625,0.5375],
254:[0.5046875,0.555989583,0.240625,0.5375],
255:[0.5046875,0.555989583,0.240625,0.5375],
256:[0.5046875,0.555989583,0.240625,0.5375],
257:[0.5046875,0.555989583,0.240625,0.5375],
258:[0.5046875,0.555989583,0.240625,0.5375],
259:[0.5046875,0.555989583,0.240625,0.5375],
260:[0.5046875,0.555989583,0.240625,0.5375],
261:[0.5046875,0.555989583,0.240625,0.5375],
262:[0.5046875,0.555989583,0.240625,0.5375],
263:[0.5046875,0.555989583,0.240625,0.5375],
264:[0.5046875,0.555989583,0.240625,0.5375]
}

# Go through the data table above and create the images
print ("Adding images...")
tagged_images_with_regions = []

video_name = "video (1)"
file_name = base_frm_url + video_name + "\\frame"

for frm_num in standing_image_regions.keys():
    if frm_num > 128:
        x,y,w,h = standing_image_regions[frm_num]
        regions = [ Region(tag_id=standing_tag.id, left=x,top=y,width=w,height=h)]

        with open(file_name + str(frm_num-1) + ".jpg", mode="rb") as image_contents:
            tagged_images_with_regions.append(ImageFileCreateEntry(name=frm_num, contents=image_contents.read(), regions=regions))
        

for frm_num in falling_image_regions.keys():
    if frm_num < 160:
        x,y,w,h = falling_image_regions[frm_num]
        regions = [ Region(tag_id=falling_tag.id, left=x,top=y,width=w,height=h)]

        with open(file_name + str(frm_num-1) + ".jpg", mode="rb") as image_contents:
            tagged_images_with_regions.append(ImageFileCreateEntry(name=frm_num, contents=image_contents.read(), regions=regions))

for frm_num in fallen_image_regions.keys():
    if frm_num < 184:
        x,y,w,h = fallen_image_regions[frm_num]
        regions = [ Region(tag_id=fallen_tag.id, left=x,top=y,width=w,height=h)]

        with open(file_name + str(frm_num-1) + ".jpg", mode="rb") as image_contents:
            tagged_images_with_regions.append(ImageFileCreateEntry(name=frm_num, contents=image_contents.read(), regions=regions))

print(len(tagged_images_with_regions))
trainer.create_images_from_files(project.id, images=tagged_images_with_regions)

# Training the custom vision classifier

import time

print ("Training...")
iteration = trainer.train_project(project.id)
while (iteration.status != "Completed"):
    iteration = trainer.get_iteration(project.id, iteration.id)
    print ("Training status: " + iteration.status)
    time.sleep(1)

# The iteration is now trained. Make it the default project endpoint
trainer.update_iteration(project.id, iteration.id, is_default=True)
print ("Done!")

#Produce predictions for new frame sequences

test_home_url = "C:\\Users\\91987\\Documents\\Oxford\\HackCambridge\\hack\\"

test_vid_url = base_home_url + "Videos\\"
test_frm_url = base_home_url + "frames\\"

ENDPOINT = "https://southcentralus.api.cognitive.microsoft.com"
prediction_key = "fdc8548027114381bd41337662282bc5"
projectId = "fa50ff7c-c909-4038-bc16-f1b929621ab3"

from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient

# Now there is a trained endpoint that can be used to make a prediction
predictor = CustomVisionPredictionClient(prediction_key, endpoint=ENDPOINT)

# Open the sample image and get back the prediction results.
for i in range(811):
    with open(test_frm_url + "video (28).avi\\" + "frame"+str(i) + ".jpg", mode="rb") as test_data:
        results = predictor.predict_image(projectId, test_data)
    
    maxTag = ""
    maxConfidence = 0
    bL = 0
    bT = 0
    bW = 0
    bH = 0
    # Display the results.
    for prediction in results.predictions:
        if prediction.probability > maxConfidence:
            maxTag = prediction.tag_name
            maxConfidence = prediction.probability
            bL = prediction.bounding_box.left
            bT = prediction.bounding_box.top
            bW = prediction.bounding_box.width
            bH = prediction.bounding_box.height

    print ("\t" + maxTag + ": {0:.2f}%".format(maxConfidence * 100), bL, bR, bW, bH)
