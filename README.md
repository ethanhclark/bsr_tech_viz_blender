# Blue Sky Robotics - Robotic Animation Pipeline Tools
Pipeline tools for UFACTORY xArm6 technical visualizations at Blue Sky Robotics. Fully rigged 6 DOF robotic arms in Blender 4.2 can be found under <strong>3D_files</strong>. Python scripts for importing/exporting rotation data via CSV can be found under <strong>scripts</strong>.
<br>

<img width="608" alt="selection" src="https://github.com/user-attachments/assets/1c51a8fc-f7f0-4e94-a637-55394db7a754" />

<h1>How to Install + Use Add-on</h1>
<ul>
  <li>Download a zip file of this repository</li>
  <li>In Blender, go to <strong>Edit -> Preferences -> Add-ons -> Install From disk (under down arrow in top right corner) -> select downloaded zip file</strong></li>
  <li>Now, in the Blender viewport, type <strong>N</strong> to pull up the sidebar. You should see a tab entitled <strong>CSV Tools</strong></li>  
  <li>To export animation data, select all six joint controllers and click <strong>Export CSV</strong>(recommend saving selection using selection sets add-on: https://captainhansode.gumroad.com/l/wqaMJ?layout=profile&recommended_by=library). You will be prompted to choose the export location - choose the desired output folder and click <strong>Export CSV</strong></li>
  <li>To import animation data, click <strong>Import CSV</strong>. You will be prompted to located the CSV file on your machine - choose the desired CSV file and click <strong>Import CSV.</strong></li>

</ul>

<h1>How to Export CSV Data (Only Using Script)</h1>
<ul>
  <li>Select all six joint controllers (recommend saving selection using selection sets add-on: https://captainhansode.gumroad.com/l/wqaMJ?layout=profile&recommended_by=library)</li>
  <li>Under <strong>Output Properties</strong>, set the export location under the output filepath dialog box (see figure below)</li>
  <li>Open <strong>export-csv.py</strong> in Scripting tab</li>
  <li>Click <strong>Run Script</strong> button</li>
  <li>Exported CSV file (<strong>rotation-data-YYMMDD</strong>) can be found at set export location</li>
  <br>
  <img width="1217" alt="export-filepath" src="https://github.com/user-attachments/assets/c0746a98-f8eb-46da-83b0-be7b900df142" />
</ul>

<h1>How to Import CSV Data (Only Using Script)</h1>
<ul>
  <li>Open <strong>import-csv.py</strong> in Scripting tab</li>
  <li>On line 32, replace the current file path with the full file path of CSV file to import (see figure below)</li>
  <li>Click <strong>Run Script</strong> button</li>
</ul>
<img width="968" alt="import-filepath" src="https://github.com/user-attachments/assets/5c39b42d-c979-4697-bb32-2b2892e5ea32" />

<br>
Coming soon: IK/FK switching on robotic rig
