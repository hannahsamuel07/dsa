class Solution(object):
    def countSegments(self, s):
        mystr = ""
        List = []
        for i in range(len(s)):
            if s[i] != ' ': # check if its a space
                mystr += s[i] # keep track of the chars
            else:
                if mystr != "": # add to the str if its note whitespace # handling trailing white spaces
                    List.append(mystr)
                mystr = ""
        if mystr != "":
            List.append(mystr)

        return len(List)