class Topic:
    """
    Includes topic class definition and functions.
    
    Parameters
    ----------
    index: count the number of User created
    topics: list storing all current topics
    topics_name: list storing all topic names
    """
    
    topics = [] # store all topic objects
    topics_name = [] # store all topic names (tname)
    index = 1
    def __init__(self, tname, user):
        """
        Define class topic
        
        Parameters
        ----------
        tname: the name of topic
        tid: the id of topic (unique)
        tag: tag/label of topic (private variable)
        """
        if tname not in Topic.topics_name:
            self.tid = Topic.index
            Topic.index += 1
            self.tname = tname
            Topic.topics.append(self)
            Topic.topics_name.append(tname)
            self.user = user
            self._tag=""
    @property
    def tag(self):
        return self._tag
    @tag.setter
    def tag(self, tag):
        # error and exception handler - 4
        try:
            tag = str(tag)
        except TypeError:
            print('TypeError occurred')
        except:
            print('Other error occurred')
        else:
            self._tag = tag
    
    def show(self):
        """
        Display topic info
        
        Returns
        ----------
        The string showing topic id and name.
        """
        return f'Topic id: {self.tid} Topic name: {self.tname}'
    
    def search(tag):
        """
        Display all topic with a given tag
        
        Returns
        ----------
        The string showing all topics' id and name under a given tag or indicating there is no topic under the given tag.
        """
        exist = 0
        for i in Topic.topics:
            if i.tag == tag:
                exist = 1
                return i.show()
        if exist == 0:
            return('[No topic under this tag.]')

# topics
topic1 = Topic('DATA533 Collaborative Software Development', 'khaladhasan')
topic1.tag = 'DATA533'
topic2 = Topic('DATA571 Resampling and Regularization', 'jeffandrews')
topic2.tag = 'DATA571'
topic3 = Topic('DATA532 Data Structure and Algorithm', 'gemarodriguezperez')
topic3.tag = 'DATA532'
topic4 = Topic('DATA540 Databases and Data Retrievel', 'ifeomaadaji')
topic4.tag = 'DATA540'
topic5 = Topic('DATA570 Predictive Modelling', 'johnthompson')
topic5.tag = 'DATA570'
topic6 = Topic('DATA543 Data Collection', 'emeliegustafsson')
topic6.tag = 'DATA543'
topic7 = Topic('DATA553 Privacy, Security and Professional Ethics', 'patricialassere')
topic7.tag = 'DATA553'
topic8 = Topic('DATA533 Project', 'amethyst1016')
topic8.tag = 'DATA533'
topic9 = Topic('DATA533 Project Group 8', 'madison13g')
topic9.tag = 'DATA533'
topic10 = Topic('General', 'christeldeas')
topic10.tag = 'MDS'