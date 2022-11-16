import unittest
import csv_to_html


class TestCSVToHTML(unittest.TestCase):
    def test_parse_csv_as_dictionary(self):
        dictionary_list = list(csv_to_html.parse_csv_as_dictionary('test.csv'))

        self.assertEqual(dictionary_list[0], {
            '1': '1',
            '2': 'Eldon Base for stackable storage shelf, platinum',
            '3': 'Muhammed MacIntyre',
            '4': '3',
            '5': '-213.25',
            '6': '38.94',
            '7': '35',
            '8': 'Nunavut',
            '9': 'Storage & Organization',
            '10': '0.8'
        })

    def test_parse_csv_as_html_string(self):
        html_string = csv_to_html.parse_csv_as_html_string('test.csv')

        self.assertEqual(html_string, '<table><thead><tr><th>1</th><th>2</th><th>3</th><th>4</th><th>5</th><th>6</th><th>7</th><th>8</th><th>9</th><th>10</th></tr></thead><tbody><tr><td>1</td><td>Eldon Base for stackable storage shelf, platinum</td><td>Muhammed MacIntyre</td><td>3</td><td>-213.25</td><td>38.94</td><td>35</td><td>Nunavut</td><td>Storage &amp; Organization</td><td>0.8</td></tr><tr><td>2</td><td>1.7 Cubic Foot Compact &quot;Cube&quot; Office Refrigerators</td><td>Barry French</td><td>293</td><td>457.81</td><td>208.16</td><td>68.02</td><td>Nunavut</td><td>Appliances</td><td>0.58</td></tr><tr><td>3</td><td>Cardinal Slant-Dï¿½ Ring Binder, Heavy Gauge Vinyl</td><td>Barry French</td><td>293</td><td>46.71</td><td>8.69</td><td>2.99</td><td>Nunavut</td><td>Binders and Binder Accessories</td><td>0.39</td></tr><tr><td>4</td><td>R380</td><td>Clay Rozendal</td><td>483</td><td>1198.97</td><td>195.99</td><td>3.99</td><td>Nunavut</td><td>Telephones and Communication</td><td>0.58</td></tr><tr><td>5</td><td>Holmes HEPA Air Purifier</td><td>Carlos Soltero</td><td>515</td><td>30.94</td><td>21.78</td><td>5.94</td><td>Nunavut</td><td>Appliances</td><td>0.5</td></tr><tr><td>6</td><td>G.E. Longer-Life Indoor Recessed Floodlight Bulbs</td><td>Carlos Soltero</td><td>515</td><td>4.43</td><td>6.64</td><td>4.95</td><td>Nunavut</td><td>Office Furnishings</td><td>0.37</td></tr><tr><td>7</td><td>Angle-D Binders with Locking Rings, Label Holders</td><td>Carl Jackson</td><td>613</td><td>-54.04</td><td>7.3</td><td>7.72</td><td>Nunavut</td><td>Binders and Binder Accessories</td><td>0.38</td></tr><tr><td>8</td><td>SAFCO Mobile Desk Side File, Wire Frame</td><td>Carl Jackson</td><td>613</td><td>127.70</td><td>42.76</td><td>6.22</td><td>Nunavut</td><td>Storage &amp; Organization</td><td></td></tr><tr><td>9</td><td>SAFCO Commercial Wire Shelving, Black</td><td>Monica Federle</td><td>643</td><td>-695.26</td><td>138.14</td><td>35</td><td>Nunavut</td><td>Storage &amp; Organization</td><td></td></tr><tr><td>10</td><td>Xerox 198</td><td>Dorothy Badders</td><td>678</td><td>-226.36</td><td>4.98</td><td>8.33</td><td>Nunavut</td><td>Paper</td><td>0.38</td></tr><tr><td>11</td><td>Xerox 1980</td><td>Neola Schneider</td><td>807</td><td>-166.85</td><td>4.28</td><td>6.18</td><td>Nunavut</td><td>Paper</td><td>0.4</td></tr><tr><td>12</td><td>Advantus Map Pennant Flags and Round Head Tacks</td><td>Neola Schneider</td><td>807</td><td>-14.33</td><td>3.95</td><td>2</td><td>Nunavut</td><td>Rubber Bands</td><td>0.53</td></tr><tr><td>13</td><td>Holmes HEPA Air Purifier</td><td>Carlos Daly</td><td>868</td><td>134.72</td><td>21.78</td><td>5.94</td><td>Nunavut</td><td>Appliances</td><td>0.5</td></tr><tr><td>14</td><td>DS/HD IBM Formatted Diskettes, 200/Pack - Staples</td><td>Carlos Daly</td><td>868</td><td>114.46</td><td>47.98</td><td>3.61</td><td>Nunavut</td><td>Computer Peripherals</td><td>0.71</td></tr><tr><td>15</td><td>Wilson Jones 1&quot; Hanging DublLockï¿½ Ring Binders</td><td>Claudia Miner</td><td>933</td><td>-4.72</td><td>5.28</td><td>2.99</td><td>Nunavut</td><td>Binders and Binder Accessories</td><td>0.37</td></tr><tr><td>16</td><td>Ultra Commercial Grade Dual Valve Door Closer</td><td>Neola Schneider</td><td>995</td><td>782.91</td><td>39.89</td><td>3.04</td><td>Nunavut</td><td>Office Furnishings</td><td>0.53</td></tr><tr><td>17</td><td>#10-4 1/8&quot; x 9 1/2&quot; Premium Diagonal Seam Envelopes</td><td>Allen Rosenblatt</td><td>998</td><td>93.80</td><td>15.74</td><td>1.39</td><td>Nunavut</td><td>Envelopes</td><td>0.4</td></tr><tr><td>18</td><td>Hon 4-Shelf Metal Bookcases</td><td>Sylvia Foulston</td><td>1154</td><td>440.72</td><td>100.98</td><td>26.22</td><td>Nunavut</td><td>Bookcases</td><td>0.6</td></tr><tr><td>19</td><td>Lesro Sheffield Collection Coffee Table, End Table, Center Table, Corner Table</td><td>Sylvia Foulston</td><td>1154</td><td>-481.04</td><td>71.37</td><td>69</td><td>Nunavut</td><td>Tables</td><td>0.68</td></tr><tr><td>20</td><td>g520</td><td>Jim Radford</td><td>1344</td><td>-11.68</td><td>65.99</td><td>5.26</td><td>Nunavut</td><td>Telephones and Communication</td><td>0.59</td></tr><tr><td>21</td><td>LX 788</td><td>Jim Radford</td><td>1344</td><td>313.58</td><td>155.99</td><td>8.99</td><td>Nunavut</td><td>Telephones and Communication</td><td>0.58</td></tr><tr><td>22</td><td>Avery 52</td><td>Carlos Soltero</td><td>1412</td><td>26.92</td><td>3.69</td><td>0.5</td><td>Nunavut</td><td>Labels</td><td>0.38</td></tr><tr><td>23</td><td>Plymouth Boxed Rubber Bands by Plymouth</td><td>Carlos Soltero</td><td>1412</td><td>-5.77</td><td>4.71</td><td>0.7</td><td>Nunavut</td><td>Rubber Bands</td><td>0.8</td></tr><tr><td>24</td><td>GBC Pre-Punched Binding Paper, Plastic, White, 8-1/2&quot; x 11&quot;</td><td>Carl Ludwig</td><td>1539</td><td>-172.88</td><td>15.99</td><td>13.18</td><td>Nunavut</td><td>Binders and Binder Accessories</td><td>0.37</td></tr><tr><td>25</td><td>Maxell 3.5&quot; DS/HD IBM-Formatted Diskettes, 10/Pack</td><td>Carl Ludwig</td><td>1539</td><td>-144.55</td><td>4.89</td><td>4.93</td><td>Nunavut</td><td>Computer Peripherals</td><td>0.66</td></tr><tr><td>26</td><td>Newell 335</td><td>Don Miller</td><td>1540</td><td>5.76</td><td>2.88</td><td>0.7</td><td>Nunavut</td><td>Pens &amp; Art Supplies</td><td>0.56</td></tr><tr><td>27</td><td>SANFORD Liquid Accentï¿½ Tank-Style Highlighters</td><td>Annie Cyprus</td><td>1702</td><td>4.90</td><td>2.84</td><td>0.93</td><td>Nunavut</td><td>Pens &amp; Art Supplies</td><td>0.54</td></tr><tr><td>28</td><td>Canon PC940 Copier</td><td>Carl Ludwig</td><td>1761</td><td>-547.61</td><td>449.99</td><td>49</td><td>Nunavut</td><td>Copiers and Fax</td><td>0.38</td></tr><tr><td>29</td><td>Tenex Personal Project File with Scoop Front Design, Black</td><td>Carlos Soltero</td><td>1792</td><td>-5.45</td><td>13.48</td><td>4.51</td><td>Nunavut</td><td>Storage &amp; Organization</td><td>0.59</td></tr><tr><td>30</td><td>Col-Eraseï¿½ Pencils with Erasers</td><td>Grant Carroll</td><td>2275</td><td>41.67</td><td>6.08</td><td>1.17</td><td>Nunavut</td><td>Pens &amp; Art Supplies</td><td>0.56</td></tr><tr><td>31</td><td>Imation 3.5&quot; DS/HD IBM Formatted Diskettes, 10/Pack</td><td>Don Miller</td><td>2277</td><td>-46.03</td><td>5.98</td><td>4.38</td><td>Nunavut</td><td>Computer Peripherals</td><td>0.75</td></tr><tr><td>32</td><td>White Dual Perf Computer Printout Paper, 2700 Sheets, 1 Part, Heavyweight, 20 lbs., 14 7/8 x 11</td><td>Don Miller</td><td>2277</td><td>33.67</td><td>40.99</td><td>19.99</td><td>Nunavut</td><td>Paper</td><td>0.36</td></tr><tr><td>33</td><td>Self-Adhesive Address Labels for Typewriters by Universal</td><td>Alan Barnes</td><td>2532</td><td>140.01</td><td>7.31</td><td>0.49</td><td>Nunavut</td><td>Labels</td><td>0.38</td></tr><tr><td>34</td><td>Accessory37</td><td>Alan Barnes</td><td>2532</td><td>-78.96</td><td>20.99</td><td>2.5</td><td>Nunavut</td><td>Telephones and Communication</td><td>0.81</td></tr><tr><td>35</td><td>Fuji 5.2GB DVD-RAM</td><td>Jack Garza</td><td>2631</td><td>252.66</td><td>40.96</td><td>1.99</td><td>Nunavut</td><td>Computer Peripherals</td><td>0.55</td></tr><tr><td>36</td><td>Bevis Steel Folding Chairs</td><td>Julia West</td><td>2757</td><td>-1766.01</td><td>95.95</td><td>74.35</td><td>Nunavut</td><td>Chairs &amp; Chairmats</td><td>0.57</td></tr><tr><td>37</td><td>Avery Binder Labels</td><td>Eugene Barchas</td><td>2791</td><td>-236.27</td><td>3.89</td><td>7.01</td><td>Nunavut</td><td>Binders and Binder Accessories</td><td>0.37</td></tr><tr><td>38</td><td>Hon Every-Dayï¿½ Chair Series Swivel Task Chairs</td><td>Eugene Barchas</td><td>2791</td><td>80.44</td><td>120.98</td><td>30</td><td>Nunavut</td><td>Chairs &amp; Chairmats</td><td>0.64</td></tr><tr><td>39</td><td>IBM Multi-Purpose Copy Paper, 8 1/2 x 11&quot;, Case</td><td>Eugene Barchas</td><td>2791</td><td>118.94</td><td>30.98</td><td>5.76</td><td>Nunavut</td><td>Paper</td><td>0.4</td></tr><tr><td>40</td><td>Global Troyï¿½ Executive Leather Low-Back Tilter</td><td>Edward Hooks</td><td>2976</td><td>3424.22</td><td>500.98</td><td>26</td><td>Nunavut</td><td>Chairs &amp; Chairmats</td><td>0.6</td></tr><tr><td>41</td><td>XtraLifeï¿½ ClearVueï¿½ Slant-Dï¿½ Ring Binders by Cardinal</td><td>Brad Eason</td><td>3232</td><td>-11.83</td><td>7.84</td><td>4.71</td><td>Nunavut</td><td>Binders and Binder Accessories</td><td>0.35</td></tr><tr><td>42</td><td>Computer Printout Paper with Letter-Trim Perforations</td><td>Nicole Hansen</td><td>3524</td><td>52.35</td><td>18.97</td><td>9.03</td><td>Nunavut</td><td>Paper</td><td>0.37</td></tr><tr><td>43</td><td>6160</td><td>Dorothy Wardle</td><td>3908</td><td>-180.20</td><td>115.99</td><td>2.5</td><td>Nunavut</td><td>Telephones and Communication</td><td>0.57</td></tr><tr><td>44</td><td>Avery 49</td><td>Aaron Bergman</td><td>4132</td><td>1.32</td><td>2.88</td><td>0.5</td><td>Nunavut</td><td>Labels</td><td>0.36</td></tr><tr><td>45</td><td>Hoover Portapowerï¿½ Portable Vacuum</td><td>Jim Radford</td><td>4612</td><td>-375.64</td><td>4.48</td><td>49</td><td>Nunavut</td><td>Appliances</td><td>0.6</td></tr><tr><td>46</td><td>Timeport L7089</td><td>Annie Cyprus</td><td>4676</td><td>-104.25</td><td>125.99</td><td>7.69</td><td>Nunavut</td><td>Telephones and Communication</td><td>0.58</td></tr><tr><td>47</td><td>Avery 510</td><td>Annie Cyprus</td><td>4676</td><td>85.96</td><td>3.75</td><td>0.5</td><td>Nunavut</td><td>Labels</td><td>0.37</td></tr><tr><td>48</td><td>Xerox 1881</td><td>Annie Cyprus</td><td>4676</td><td>-8.38</td><td>12.28</td><td>6.47</td><td>Nunavut</td><td>Paper</td><td>0.38</td></tr><tr><td>49</td><td>LX 788</td><td>Annie Cyprus</td><td>4676</td><td>1115.69</td><td>155.99</td><td>8.99</td><td>Nunavut</td><td>Telephones and Communication</td><td>0.58</td></tr><tr><td>50</td><td>Cardinal Slant-Dï¿½ Ring Binder, Heavy Gauge Vinyl</td><td>Annie Cyprus</td><td>5284</td><td>-3.05</td><td>8.69</td><td>2.99</td><td>Nunavut</td><td>Binders and Binder Accessories</td><td>0.39</td></tr><tr><td>51</td><td>Memorex 4.7GB DVD-RAM, 3/Pack</td><td>Clay Rozendal</td><td>5316</td><td>514.07</td><td>31.78</td><td>1.99</td><td>Nunavut</td><td>Computer Peripherals</td><td>0.42</td></tr><tr><td>52</td><td>Unpadded Memo Slips</td><td>Don Jones</td><td>5409</td><td>-7.04</td><td>3.98</td><td>2.97</td><td>Nunavut</td><td>Paper</td><td>0.35</td></tr><tr><td>53</td><td>Adams Telephone Message Book W/Dividers/Space For Phone Numbers, 5 1/4&quot;X8 1/2&quot;, 300/Messages</td><td>Beth Thompson</td><td>5506</td><td>4.41</td><td>5.88</td><td>3.04</td><td>Nunavut</td><td>Paper</td><td>0.36</td></tr><tr><td>54</td><td>Eldon Expressionsï¿½ Desk Accessory, Wood Pencil Holder, Oak</td><td>Frank Price</td><td>5569</td><td>-0.06</td><td>9.65</td><td>6.22</td><td>Nunavut</td><td>Office Furnishings</td><td>0.55</td></tr><tr><td>55</td><td>Bell Sonecor JB700 Caller ID</td><td>Michelle Lonsdale</td><td>5607</td><td>-50.33</td><td>7.99</td><td>5.03</td><td>Nunavut</td><td>Telephones and Communication</td><td>0.6</td></tr><tr><td>56</td><td>Avery Arch Ring Binders</td><td>Ann Chong</td><td>5894</td><td>87.68</td><td>58.1</td><td>1.49</td><td>Nunavut</td><td>Binders and Binder Accessories</td><td>0.38</td></tr><tr><td>57</td><td>APC 7 Outlet Network SurgeArrest Surge Protector</td><td>Ann Chong</td><td>5894</td><td>-68.22</td><td>80.48</td><td>4.5</td><td>Nunavut</td><td>Appliances</td><td>0.55</td></tr><tr><td>58</td><td>Deflect-o RollaMat Studded, Beveled Mat for Medium Pile Carpeting</td><td>Joy Bell</td><td>5925</td><td>-354.90</td><td>92.23</td><td>39.61</td><td>Nunavut</td><td>Office Furnishings</td><td>0.67</td></tr><tr><td>59</td><td>Accessory4</td><td>Joy Bell</td><td>5925</td><td>-267.01</td><td>85.99</td><td>0.99</td><td>Nunavut</td><td>Telephones and Communication</td><td>0.85</td></tr><tr><td>60</td><td>Personal Creationsï¿½ Ink Jet Cards and Labels</td><td>Skye Norling</td><td>6016</td><td>3.63</td><td>11.48</td><td>5.43</td><td>Nunavut</td><td>Paper</td><td>0.36</td></tr><tr><td>61</td><td>High Speed Automatic Electric Letter Opener</td><td>Barry Weirich</td><td>6116</td><td>-1759.58</td><td>1637.53</td><td>24.49</td><td>Nunavut</td><td>Scissors, Rulers and Trimmers</td><td>0.81</td></tr><tr><td>62</td><td>Xerox 1966</td><td>Grant Carroll</td><td>6182</td><td>-116.79</td><td>6.48</td><td>6.65</td><td>Nunavut</td><td>Paper</td><td>0.36</td></tr><tr><td>63</td><td>Xerox 213</td><td>Grant Carroll</td><td>6182</td><td>-67.28</td><td>6.48</td><td>7.86</td><td>Nunavut</td><td>Paper</td><td>0.37</td></tr><tr><td>64</td><td>Boston Electric Pencil Sharpener, Model 1818, Charcoal Black</td><td>Adrian Hane</td><td>6535</td><td>-19.33</td><td>28.15</td><td>8.99</td><td>Nunavut</td><td>Pens &amp; Art Supplies</td><td>0.57</td></tr><tr><td>65</td><td>Hammermill CopyPlus Copy Paper (20Lb. and 84 Bright)</td><td>Skye Norling</td><td>6884</td><td>-61.21</td><td>4.98</td><td>4.75</td><td>Nunavut</td><td>Paper</td><td>0.36</td></tr><tr><td>66</td><td>Telephone Message Books with Fax/Mobile Section, 5 1/2&quot; x 3 3/16&quot;</td><td>Skye Norling</td><td>6884</td><td>119.09</td><td>6.35</td><td>1.02</td><td>Nunavut</td><td>Paper</td><td>0.39</td></tr><tr><td>67</td><td>Crate-A-Filesï¿½</td><td>Andrew Gjertsen</td><td>6916</td><td>-141.27</td><td>10.9</td><td>7.46</td><td>Nunavut</td><td>Storage &amp; Organization</td><td>0.59</td></tr><tr><td>68</td><td>Angle-D Binders with Locking Rings, Label Holders</td><td>Ralph Knight</td><td>6980</td><td>-77.28</td><td>7.3</td><td>7.72</td><td>Nunavut</td><td>Binders and Binder Accessories</td><td>0.38</td></tr><tr><td>69</td><td>80 Minute CD-R Spindle, 100/Pack - Staples</td><td>Dorothy Wardle</td><td>6982</td><td>407.44</td><td>39.48</td><td>1.99</td><td>Nunavut</td><td>Computer Peripherals</td><td>0.54</td></tr><tr><td>70</td><td>Bush Westfield Collection Bookcases, Dark Cherry Finish, Fully Assembled</td><td>Dorothy Wardle</td><td>6982</td><td>-338.27</td><td>100.98</td><td>57.38</td><td>Nunavut</td><td>Bookcases</td><td>0.78</td></tr><tr><td>71</td><td>12-1/2 Diameter Round Wall Clock</td><td>Dorothy Wardle</td><td>6982</td><td>52.56</td><td>19.98</td><td>10.49</td><td>Nunavut</td><td>Office Furnishings</td><td>0.49</td></tr><tr><td>72</td><td>SAFCO Arco Folding Chair</td><td>Grant Carroll</td><td>7110</td><td>1902.24</td><td>276.2</td><td>24.49</td><td>Nunavut</td><td>Chairs &amp; Chairmats</td><td></td></tr><tr><td>73</td><td>#10 White Business Envelopes,4 1/8 x 9 1/2</td><td>Barry Weirich</td><td>7430</td><td>353.20</td><td>15.67</td><td>1.39</td><td>Nunavut</td><td>Envelopes</td><td>0.38</td></tr><tr><td>74</td><td>3M Office Air Cleaner</td><td>Beth Paige</td><td>7906</td><td>271.78</td><td>25.98</td><td>5.37</td><td>Nunavut</td><td>Appliances</td><td>0.5</td></tr><tr><td>75</td><td>Global Leather and Oak Executive Chair, Black</td><td>Sylvia Foulston</td><td>8391</td><td>-268.36</td><td>300.98</td><td>64.73</td><td>Nunavut</td><td>Chairs &amp; Chairmats</td><td>0.56</td></tr><tr><td>76</td><td>Xerox 1936</td><td>Nicole Hansen</td><td>8419</td><td>70.39</td><td>19.98</td><td>5.97</td><td>Nunavut</td><td>Paper</td><td>0.38</td></tr><tr><td>77</td><td>Xerox 214</td><td>Nicole Hansen</td><td>8419</td><td>-86.62</td><td>6.48</td><td>7.03</td><td>Nunavut</td><td>Paper</td><td>0.37</td></tr><tr><td>78</td><td>Carina Double Wide Media Storage Towers in Natural &amp; Black</td><td>Nicole Hansen</td><td>8833</td><td>-846.73</td><td>80.98</td><td>35</td><td>Nunavut</td><td>Storage &amp; Organization</td><td>0.81</td></tr><tr><td>79</td><td>Staplesï¿½ General Use 3-Ring Binders</td><td>Beth Paige</td><td>8995</td><td>8.05</td><td>1.88</td><td>1.49</td><td>Nunavut</td><td>Binders and Binder Accessories</td><td>0.37</td></tr><tr><td>80</td><td>Xerox 1904</td><td>Beth Paige</td><td>8995</td><td>-78.02</td><td>6.48</td><td>5.86</td><td>Northwest Territories</td><td>Paper</td><td>0.36</td></tr><tr><td>81</td><td>Luxo Professional Combination Clamp-On Lamps</td><td>Beth Paige</td><td>8995</td><td>737.94</td><td>102.3</td><td>21.26</td><td>Northwest Territories</td><td>Office Furnishings</td><td>0.59</td></tr><tr><td>82</td><td>Xerox 217</td><td>Beth Paige</td><td>8995</td><td>-191.28</td><td>6.48</td><td>8.19</td><td>Northwest Territories</td><td>Paper</td><td>0.37</td></tr><tr><td>83</td><td>Revere Boxed Rubber Bands by Revere</td><td>Beth Paige</td><td>8995</td><td>-21.49</td><td>1.89</td><td>0.76</td><td>Northwest Territories</td><td>Rubber Bands</td><td>0.83</td></tr><tr><td>84</td><td>Acco Smartsocketï¿½ Table Surge Protector, 6 Color-Coded Adapter Outlets</td><td>Sylvia Foulston</td><td>9126</td><td>884.08</td><td>62.05</td><td>3.99</td><td>Northwest Territories</td><td>Appliances</td><td>0.55</td></tr><tr><td>85</td><td>Tennsco Snap-Together Open Shelving Units, Starter Sets and Add-On Units</td><td>Bryan Davis</td><td>9127</td><td>-329.49</td><td>279.48</td><td>35</td><td>Northwest Territories</td><td>Storage &amp; Organization</td><td>0.8</td></tr><tr><td>86</td><td>Hon 4070 Series Pagodaï¿½ Round Back Stacking Chairs</td><td>Joy Bell</td><td>9509</td><td>2825.15</td><td>320.98</td><td>58.95</td><td>Northwest Territories</td><td>Chairs &amp; Chairmats</td><td>0.57</td></tr><tr><td>87</td><td>Xerox 1887</td><td>Joy Bell</td><td>9509</td><td>2.13</td><td>18.97</td><td>5.21</td><td>Northwest Territories</td><td>Paper</td><td>0.37</td></tr><tr><td>88</td><td>Xerox 1891</td><td>Joy Bell</td><td>9509</td><td>707.15</td><td>48.91</td><td>5.81</td><td>Northwest Territories</td><td>Paper</td><td>0.38</td></tr><tr><td>89</td><td>Avery 506</td><td>Alan Barnes</td><td>9763</td><td>75.13</td><td>4.13</td><td>0.5</td><td>Northwest Territories</td><td>Labels</td><td>0.39</td></tr><tr><td>90</td><td>Bush Heritage Pine Collection 5-Shelf Bookcase, Albany Pine Finish, *Special Order</td><td>Grant Carroll</td><td>9927</td><td>-270.63</td><td>140.98</td><td>53.48</td><td>Northwest Territories</td><td>Bookcases</td><td>0.65</td></tr><tr><td>91</td><td>Lifetime Advantageï¿½ Folding Chairs, 4/Carton</td><td>Grant Carroll</td><td>9927</td><td>3387.35</td><td>218.08</td><td>18.06</td><td>Northwest Territories</td><td>Chairs &amp; Chairmats</td><td>0.57</td></tr><tr><td>92</td><td>Microsoft Natural Multimedia Keyboard</td><td>Grant Carroll</td><td>9927</td><td>-82.16</td><td>50.98</td><td>6.5</td><td>Northwest Territories</td><td>Computer Peripherals</td><td>0.73</td></tr><tr><td>93</td><td>Staples Wirebound Steno Books, 6&quot; x 9&quot;, 12/Pack</td><td>Delfina Latchford</td><td>10022</td><td>-3.88</td><td>10.14</td><td>2.27</td><td>Northwest Territories</td><td>Paper</td><td>0.36</td></tr><tr><td>94</td><td>GBC Pre-Punched Binding Paper, Plastic, White, 8-1/2&quot; x 11&quot;</td><td>Don Jones</td><td>10437</td><td>-191.22</td><td>15.99</td><td>13.18</td><td>Northwest Territories</td><td>Binders and Binder Accessories</td><td>0.37</td></tr><tr><td>95</td><td>Bevis Boat-Shaped Conference Table</td><td>Doug Bickford</td><td>10499</td><td>31.21</td><td>262.11</td><td>62.74</td><td>Northwest Territories</td><td>Tables</td><td>0.75</td></tr><tr><td>96</td><td>Lindenï¿½ 12&quot; Wall Clock With Oak Frame</td><td>Doug Bickford</td><td>10535</td><td>-44.14</td><td>33.98</td><td>19.99</td><td>Northwest Territories</td><td>Office Furnishings</td><td>0.55</td></tr><tr><td>97</td><td>Newell 326</td><td>Doug Bickford</td><td>10535</td><td>-0.79</td><td>1.76</td><td>0.7</td><td>Northwest Territories</td><td>Pens &amp; Art Supplies</td><td>0.56</td></tr><tr><td>98</td><td>Prismacolor Color Pencil Set</td><td>Jamie Kunitz</td><td>10789</td><td>76.42</td><td>19.84</td><td>4.1</td><td>Northwest Territories</td><td>Pens &amp; Art Supplies</td><td>0.44</td></tr><tr><td>99</td><td>Xerox Blank Computer Paper</td><td>Anthony Johnson</td><td>10791</td><td>93.36</td><td>19.98</td><td>5.77</td><td>Northwest Territories</td><td>Paper</td><td>0.38</td></tr><tr><td>100</td><td>600 Series Flip</td><td>Ralph Knight</td><td>10945</td><td>4.22</td><td>95.99</td><td>8.99</td><td>Northwest Territories</td><td>Telephones and Communication</td><td>0.57</td></tr></tbody></table>')