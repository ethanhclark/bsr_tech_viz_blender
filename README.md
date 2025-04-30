<h1>Blue Sky Robotics - 3D Files Overview</h1>
<p>General Overview of 3D files for Blue Sky Robotics visualization pipeline.</p>
<br>
<p>In this repo, there are six Blender 4.2.1 Files under <strong>3D_files</strong>:</p>

<ul>
  <li>arm-ik-fk.blend</li>
  <li>arm-gripper-core.blend</li>
  <li>arm-vacuum-core.blend</li>
  <li>arm-spraybot-core.blend</li>
  <li>arm-spraybot-inverted-core.blend</li>
  <li>arm-gripper-chain.blend</li>
</ul>
<hr>
<img width="481" alt="ref-pic-1" src="https://github.com/user-attachments/assets/f90351b3-d959-4f84-97ef-21e811eee5ff" />

<h2>arm-ik-fk.blend</h2>
<p><i>Follow along with these textual instructions by referencing the following video: https://youtu.be/F5-9ONM91Xo?si=9xREusXVNDrOoQ4q</i></p>

<p>In this file, the xARM6 robotic arm with the spraybot end effector is fully set up with an IK/FK rig + switch for general animation.</p>
<p>To animate the robot in the same way we create profiles with the physical robot in manual mode (IK Rig):</p>
<ul>
  <li>Select the square directly below the end effector named <strong>CTRL_IK</strong></li>
  <li>Under the <strong>Object Properties</strong> window (orange square icon), scroll all the way down to the <strong>Custom Properties</strong> section and locate the <strong>IK_FK_Switch</strong> property</li>
  <li>Ensure that the property value is set to 0 (<strong>manual mode/IK animation: IK_FK_Switch = 0. Individual joint/FK animation: IK_FK_Switch = 1</strong></li>
  <li>Once this has been set, click <strong>G</strong> (for grab and move) - you'll be able to manipulate the robotic arm now and can keyframe this object to create animation profiles.</li>
  <ul>
    <li>Reminder: to lock movement along a specific world axis, click <strong>G</strong>, then either <strong>X, Y, or Z</strong> to lock movement along that world axis. To lock movement along the object's local axis, click <strong>G</strong>, then either <strong>X, Y, or Z twice</strong> to lock movement along that object's local axis. </li>
  </ul>
</ul>
<p>To animate the robot by moving each individual joint (FK Rig):</p>
<ul>
  <li>Select the square directly below the end effector named <strong>CTRL_IK</strong></li>
  <li>Under the <strong>Object Properties</strong> window (orange square icon), scroll all the way down to the <strong>Custom Properties</strong> section and locate the <strong>IK_FK_Switch</strong> property</li>
  <li>Ensure that the property value is set to 1 (<strong>manual mode/IK animation: IK_FK_Switch = 0. Individual joint/FK animation: IK_FK_Switch = 1</strong></li>
  <li>Once this has been set, click <strong>R</strong> (for rotate) - you'll be able to manipulate the robotic arm now and can keyframe <strong>each individual control circle</strong> to create animation profiles.</li>
</ul>
</p>
<hr>

![arm-gripper-core](https://github.com/user-attachments/assets/bcb4110a-0c7e-433a-b642-1c8522ef96a2)

<h2>arm-gripper-core.blend & arm-vacuum-core.blend</h2>
<p><i>Follow along with these textual instructions by referencing the following video: https://youtu.be/RzfJpirGwIM</i></p>

<p>In these files, the xARM6 robotic arm with either the gripper end effector or vacuum end effector is fully set up with a FK rig + basic lighting + a camera for rendering.</p>
<p>To animate the robot and/or create renders of this robot, refer to the following general notes:</p>
<ul>
  <li>Under the <strong>Robotic Arm</strong> collection, you can see the <strong>CTRL_Move</strong> object - if you select his object, you will be able to move and animate the location of the entire robot. Always keep the <strong>camera</strong> icon unchecked so that it does not show in final renders.</li>
  <li>You should not need to access anything in the hidden <strong>References</strong> collection - these objects were for the creation of the original robot arm object</li>
  <li>Under the <strong>Rendering</strong> collection, you can adjust the following three settings for rendering:</li>
  <ol>
    <li><strong>Render Camera</strong></li>
    <ul>
      <li>You can adjust the render camera settings by selecting <strong>render-camera</strong>, then navigating to the camera settings (camera icon). These settings should be set up and good to go by default, but there are many YouTube tutorials on settings you can modify in this tab to adjust different aspects of your final render.</li>
      <li>I normally have another 3D viewport in my Blender window that shows a preview of what the final render will look like. To set this up, click on the camera icon in that 3D viewport, then click <strong>Viewport Shading</strong> in the top menu to view the render with proper lighting.</li>
      <li>With this viewport set up, you can click <strong>N</strong> to pull up the sidebar menu. Navigate to the <strong>View</strong> tab, then check <strong>Camera to View</strong>. Now, when you move and rotate your view in the render preview layout, the actual camera will move in 3D space and accordingly render out from the final angle you choose. <strong>Always remember</strong> to navigate back to the sidebar menu and uncheck <strong>Camera to View</strong> once you've set up your desired camera angle.</li>
    </ul>
    <li><strong>Lighting</strong></li>
    <ul>
      <li>There are three lights set up by default: <strong>light-1</strong>, <strong>light-2</strong>, and <strong>light-3</strong>. You can select any of these three lights, then click on the lightbulb icon to navigate to the light's settings. Here you can modify the light's brightness and color, along with several other settings. This falls more into the creative category more than technical, but there are several YouTube tutorials online as well for setting up general lighting in Blender.</li>
      <li>To create a new light, click on the <strong>Add</strong> on the top menu, and navigate to the <strong>Light</strong> button, then select your light type. I tend to use <strong>Spot</strong> lights, but again you can reference outside YouTube tutorials on the pros and cons of each of the different light types.</li>
      <li>Lights can be moved and rotated the same as any other 3D object using the <strong>G</strong> and <strong>R</strong> hotkeys. With your final render preview window set up, you can hide and unhide certain lights by clicking the <strong>eyeball</strong> icon to see the effects of each light on the final render. When you're ready to render out the final image, make sure you have the <strong>camera</strong> icon next to each light accordingly checked or unchecked, depending on whether or not you want each light to be on for the final render.</li>
      <li>Each scene also has a default HDRI light set up to provide general ambient light for the render. To view this, navigate to the <strong>Shading</strong> tab on the top menu, then in the node editor navigate to the <strong>World</strong> tab under the <strong>Shading Type</strong> window. Each scene should already be set up with a default HDRI. If you want to adjust the brightness of the ambient lighting, locate the green <strong>Background</strong> node, then adjust the <strong>Strength</strong> attribute to adjust the brightness of the light. I recommend keeping it below 1.3 at all times to keep your renders realistic. </li>
      <ul>
        <li>If you wish to find and use a different HDRI, I recommend looking on the Poly Haven website at the following link: https://polyhaven.com/hdris. When prompted to download a selected HDRI, always make sure the format is <strong>HDR</strong> instead of EXR, and select <strong>1K</strong> for the resolution.</li>
      </ul>
    </ul>
    <li><strong>Scenic Elements</strong></li>
    <ul>
      <li>In these scenes, there is a default <strong>floor</strong>, <strong>wall-1</strong>, and <strong>wall-2</strong> set up as a backdrop for your render. These can be shown/hidden by clicking the <strong>eyeball</strong> icon next to each object. You can also change the material properties of the walls and floor by selecting the desired object, then navigating to the <strong>Materials</strong> tab (red checkered sphere icon). I normally only adjust the <strong>Base Color</strong>, <strong>Metallic</strong>, and <strong>Roughness</strong> properties to achieve the desired look for the background.</li>
    </ul>
  </ol>
</ul>
<p>To render out a final image:</p>
<ol>
  <li>Navigate to the <strong>Render</strong> tab in the bottom right menu.</li>
  <li>Select <strong>Cycles</strong> for the render engine and set the Device to <strong>CPU</strong> (unless you're rending on a computer with a graphics card - in that case, select <strong>GPU Compute</strong>)</li>
  <li>Ensure that under the <strong>Sampling</strong> -> <strong>Render</strong> dropdown menu, ensure that the <strong>Max Samples</strong> is set to either <strong>64</strong> or <strong>128</strong> (depending on the quality level desired - I normally don't set it to anything above 128).</li>
  <li>Ensure that the <strong>Denoise</strong> checkbox is also checked under the <strong>Sampling</strong> -> <strong>Render</strong> dropdown menu.</li>
  <li>Then, in the top left menu bar, click <strong>Render</strong>, then <strong>Render Image</strong>.</li>
  <li>You'll see the render progress (Sample ##/64/128), along with the time remaining on the render. Once the image has fully rendered out, click <strong>Image</strong> -> <strong>Save AS</strong> to save your image to the desired location on your machine.</li>
</ol>
<p>To render out a final animation:</p>
<ol>
  <li>Navigate to the <strong>Render</strong> tab in the bottom right menu (camera icon).</li>
  <li>Select <strong>Cycles</strong> for the render engine and set the Device to <strong>CPU</strong> (unless you're rending on a computer with a graphics card - in that case, select <strong>GPU Compute</strong>)</li>
  <li>Ensure that under the <strong>Sampling</strong> -> <strong>Render</strong> dropdown menu, ensure that the <strong>Max Samples</strong> is set to either <strong>64</strong> or <strong>128</strong> (depending on the quality level desired - I normally don't set it to anything above 128).</li>
  <li>Ensure that the <strong>Denoise</strong> checkbox is also checked under the <strong>Sampling</strong> -> <strong>Render</strong> dropdown menu.</li>
  <li>Then, navigate to the <strong>Output</strong> tab in the bottom right menu (printer icon)</li>
  <li>Under the <strong>Output</strong> dropdown menu, ensure that the file path is set to the desired folder to which you want to export your animation. I always create a new folder for each animation to store each of the rendered frames.</li>
  <li>Before rendering the animation, make sure the <strong>Start</strong> and <strong>End</strong> frame parameters are set to the desired range in your <strong>Timeline</strong> window. If your animation only lasts 90 frames for example - but the frame range is set from 0 to 250 - then Blender will render out 160 extra frames of the scene sitting motionless because it thinks the animation lasts for 250 frames.</li>
  <li>Finally, in the top left menu bar, click <strong>Render</strong>, then <strong>Render Animation</strong>.</li>
  <li>You'll see the render progress (Sample ##/64/128) for each frame, along with the time remaining on the render for each frame.</li>
  <li>Once your entire animation has rendered out, you should see an image for each individual frame in your new folder. To export these frames as a final MP4 file, open Premiere Pro and create a new project.</li>
  <li>Go to <strong>Import Media</strong>, then open your folder with the animation frames.</li>
  <li>Select <strong>only</strong> the first image in the folder</li>
  <li>Open the <strong>Show Options</strong> dropdown menu, and check <strong>Image Sequence</strong>. Once this box is checked, you can then click <strong>Import</strong></li>
  <li>You can then bring the video into a new sequence, preview the full animation, and export it as a MP4 from Premiere.</li>
</ol>
<hr>
<img width="1000" alt="arm-spraybot-core" src="https://github.com/user-attachments/assets/8ff7e00a-83f0-43c0-a1e8-43a5b1b765c0" />


<h2>arm-spraybot-core.blend + arm-spraybot-inverted-core.blend + arm-gripper-chain</h2>

<p>Everything in these  files should be identical to the notes in the previous section pertaning to arm-gripper-core.blend & arm-vacuum-core.blend. The following bullet points are notes on a few minor differences/additions found in these files.</p>
<p><strong>arm-spraybot-core.blend:</strong></p>
<ul>
  <li>In this file, there is a <strong>Scenic Elements</strong> collection that has four objects in it: <strong>perp-rail</strong>, <strong>rail</strong>, <strong>side-rails</strong>, and <strong>wire-tray</strong>. These items are included for renders of the spraybot in an example environment.</li>
  <li>Since this scene has the robot set up on a rail, the movement of the robotic arm is locked so that it can only be moved along the rail. If you wish to disable this constraint, select <strong>CTRL_Move</strong>, and navigate to the <strong>Object Properties</strong> tab. Next to <strong>Location Y and Z</strong>, you can click the lock icons to the right to release the movement constraints along these axes</li>
</ul>
<p><strong>arm-spraybot-inverted-core.blend:</strong></p>
<ul>
  <li>In this file, there is a <strong>Scenic Elements</strong> collection that has several objects in it. These items are included for renders of the spraybot in an example environment.</li>
  <li>Since this scene has the robot set up on a rail, the movement of the robotic arm is locked so that it can only be moved along the rail. If you wish to disable this constraint, select <strong>CTRL_Move</strong>, and navigate to the <strong>Object Properties</strong> tab. Next to <strong>Location Y and Z</strong>, you can click the lock icons to the right to release the movement constraints along these axes</li>
</ul>
<p><strong>arm-gripper-chain:</strong></p>
<ul>
  <li>In this file, there are five robotic arms set up in a row for rendering out images that require multiple robotic arms in the composition.</li>
  <li>There is a new collection in this file: <strong>Duplicate Arms</strong>, which contains the four extra robotic arms created for this composition.</li>
</ul>

<hr>
<img width="608" alt="selection" src="https://github.com/user-attachments/assets/1c51a8fc-f7f0-4e94-a637-55394db7a754" />

<h1>Import/Export Animation Data Pipeline Tools</h1>
Pipeline tools for UFACTORY xArm6 technical visualizations at Blue Sky Robotics. Fully rigged 6 DOF robotic arms in Blender 4.2 can be found under <strong>3D_files</strong>. Python scripts for importing/exporting rotation data via CSV can be found under <strong>scripts</strong>.
<br>
<h2>How to Install + Use Add-on</h2>
<ul>
  <li>Download a zip file of this repository</li>
  <li>In Blender, go to <strong>Edit -> Preferences -> Add-ons -> Install From disk (under down arrow in top right corner) -> select downloaded zip file</strong></li>
  <li>Now, in the Blender viewport, type <strong>N</strong> to pull up the sidebar. You should see a tab entitled <strong>CSV Tools</strong></li>  
  <li>To export animation data, select all six joint controllers and click <strong>Export CSV</strong>(recommend saving selection using selection sets add-on: https://captainhansode.gumroad.com/l/wqaMJ?layout=profile&recommended_by=library). You will be prompted to choose the export location - choose the desired output folder and click <strong>Export CSV</strong></li>
  <li>To import animation data, click <strong>Import CSV</strong>. You will be prompted to located the CSV file on your machine - choose the desired CSV file and click <strong>Import CSV.</strong></li>

</ul>

<h2>How to Export CSV Data (Only Using Script)</h2>
<ul>
  <li>Select all six joint controllers (recommend saving selection using selection sets add-on: https://captainhansode.gumroad.com/l/wqaMJ?layout=profile&recommended_by=library)</li>
  <li>Under <strong>Output Properties</strong>, set the export location under the output filepath dialog box (see figure below)</li>
  <li>Open <strong>export-csv.py</strong> in Scripting tab</li>
  <li>Click <strong>Run Script</strong> button</li>
  <li>Exported CSV file (<strong>rotation-data-YYMMDD</strong>) can be found at set export location</li>
  <br>
  <img width="1217" alt="export-filepath" src="https://github.com/user-attachments/assets/c0746a98-f8eb-46da-83b0-be7b900df142" />
</ul>

<h2>How to Import CSV Data (Only Using Script)</h2>
<ul>
  <li>Open <strong>import-csv.py</strong> in Scripting tab</li>
  <li>On line 32, replace the current file path with the full file path of CSV file to import (see figure below)</li>
  <li>Click <strong>Run Script</strong> button</li>
</ul>
<img width="968" alt="import-filepath" src="https://github.com/user-attachments/assets/5c39b42d-c979-4697-bb32-2b2892e5ea32" />

<hr>

<img width="559" alt="path-visualization" src="https://github.com/user-attachments/assets/253fe765-bb06-452e-be43-8f76762c257b" />

<h1>Path Visualization Tool</h1>
<p><i>Follow along with these textual instructions by referencing the following video: https://youtu.be/N7qA6_AeduY?si=Ij_gVuJPQ2tFybkh</i></p>

<p>We have used another Blender plug-in to visualize the path of an animation profile in Blender, as pictured above. The link to the GitHub repo for downloading this custom plug-in can be found here: https://github.com/camkania/blender_snapshot_tool</p>
<p>To use this plug-in for our purposes, follow these steps:</p>
<ol>
  <li>Open the Blender file that contains the desired animation profile to visualize</li>
  <li>Select the end effector on the robot, specifically the object closest to the very end of the robotic arm chain</li>
  <li>Click (in this order!) <strong>Shift + S + 2</strong></li>
  <li>Now, on the top bar click <strong>Add</strong> -> <strong>Mesh</strong> -> <strong>UV Sphere</strong></li>
  <li>Then (in this order!) select the new sphere, then hold shift and select any piece on the robotic arm</li>
  <li>Click <strong>Command + P</strong>, then select <strong>Object (Keep Transform)</strong>. Now when you play the animation, the sphere should follow the path of the robotic arm.</li>
  <li>Now, select the sphere again, click <strong>N</strong> to pull up the side bar, and navigate to the <strong>Snapshot</strong> tab.</li>
  <li>Set the <strong>Start Frame</strong> and <strong>End Frame</strong> to the same range as your animation profile. Make sure the <strong>Frame Interval</strong> is set to <strong>1</strong></li>
  <li>With the sphere still selected, click the <strong>Run Snapshot Process</strong> button. This might take several moments to run.</li>
  <li>Once the script runs, click <strong>Combine Snapshots</strong>. You should now see a visualization of the robotic arm path in the 3D viewport, and a new collection entitled <strong>Snapshot_Meshes</strong> with the new object <strong>Combined_Snapshot</strong> inside.</li>
    
</ol>

<hr>
<img width="678" alt="Screenshot 2025-04-30 at 3 32 53 PM" src="https://github.com/user-attachments/assets/0ebb9d9c-6f74-43eb-a64a-a1f2e4b5667a" />

<h1>Exporting 3D Scene to Apple Vision Pro</h1>
<p>The following steps walk through how to export your 3D scene for visualization in the Apple Vision Pro (AVP). Before starting this process, make sure you have a Sketchfab account created. If not, you can create an account at the following link: https://sketchfab.com/</p>
<ol>
  <li>In your Blender file, ensure that only the objects you want to be visible in the AVP have the camera icon checked in the Scene Outliner</li>
  <li>Go to <strong>File</strong> -> <strong>Export</strong> -> <strong>glTF 2.0 (.glb/.gltf)</strong></li>
  <li>Under the <strong>Include</strong> tab: check <strong>Renderable Objects</strong> under the <strong>Limit to</strong> section.</li>
  <li>Under <strong>Data</strong> -> <strong>Mesh</strong>, make sure <strong>Apply Modifiers</strong> is checked.</li>
  <li><strong>If this is your first time exporting to AVP:</strong> check <strong>Remember Export Settings</strong> to avoid doing this process for future exports.</li>
  <img width="241" alt="avp-export-settings" src="https://github.com/user-attachments/assets/00b7a8bc-4039-426b-a0d1-c5bc53311f82" />
<li>Once exported, navigate to your Sketchfab account, click <strong>Upload</strong>, and select your <strong>.glb file</strong></li>
  <li>After the upload processes, you can click <strong>Edit 3D Settings</strong> to view a preview of the model. In this window, you can also navigate to the <strong>Materials</strong> tab (picture frame icon) to modify the material settings for each object to fine tune how it will appear on the AVP.</li>
</ol>
