#include <iostream>

using namespace std;


//Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};

class Solution {
public:
    ListNode *addTwoNumbers(ListNode *const l1, ListNode *const l2) {
        ListNode *n1 = l1;
        ListNode *n2 = l2;
        ListNode head(0);
        ListNode *res = &head;
        ListNode *tmp = &head;

        bool carry = false;
        int sum = 0;
        while (1) {
            if (n1 != nullptr && n2 != nullptr) {
                sum = carry ? n1->val + n2->val + 1 : n1->val + n2->val;


            } else if (n1 != nullptr) {
                sum = carry ? n1->val + 1 : n1->val;


            } else if (n2 != nullptr) {
                sum = carry ? n2->val + 1 : n2->val;

            } else {
                if (carry) {
                    tmp->next = new ListNode(1);
                }
                tmp = res;
                res = res->next;
                return res;
            }

            carry = is_carry(sum);
            tmp->next = new ListNode(sum);


            if (n1 != nullptr)
                n1 = n1->next;
            if (n2 != nullptr)
                n2 = n2->next;
            tmp = tmp->next;
        }
    }

    bool is_carry(int &sum) {
        if (sum >= 10) {
            sum = sum - 10;
            return true;
        } else {
            return false;
        }
    }
};


int main()
{
    ListNode *l1;
    ListNode *l2;
    ListNode *l3;
    ListNode *l4;
    ListNode *l5;
    ListNode *l6;
    ListNode *l7;

    l1 = new ListNode(2);
    l2 = new ListNode(1);
    l3 = new ListNode(9);

    l4 = new ListNode(6);
    l5 = new ListNode(6);
    l6 = new ListNode(9);
    l7 = new ListNode(7);

    l1->next = l2;
    l2->next = l3;

    l4->next = l5;
    l5->next = l6;
    l6->next = l7;


    Solution sol;
    ListNode *res = sol.addTwoNumbers(l1, l4);
    for ( ListNode *it = res; it != nullptr; it = it->next) {
        cout << it->val << endl;
    }

    return 0;
}
