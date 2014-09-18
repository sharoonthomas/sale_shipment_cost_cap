# -*- coding: utf-8 -*-
"""
    tests/test_views_depends.py

    :copyright: (C) 2014 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.
"""

# Case 1:
#
#   Sale 1 with following:
#
#       * Product 1: 10 x 5 = 50
#       * Product 2: 20 * 2 = 40
#       * Shipment : 30
#
#   Ship it as a single shipment with cost 25
#
#   Assert:
#
#       * Invoice total is 50 + 40 + 25 = 115
#
# Case 2:
#
#   Sale 1 with 2 shipments and each costs 15
#
#   Assert:
#
#       * Invoice total is (50 + 15) and (40 + 15) = 120
#
# Case 3:
#
#   Sale 1 with 3 shipment and each costs 15
#
#   Assert:
#
#       * Invoice total is (30 + 15) + (20 + 15) + (40 + 0) = 120
#
# Case 4: negative
#
#  shipment_cost_method on order and the invoice should match the sale
#
# Case 5: negative
#
#  shipment_cost_method on shipment and the invoice should reflect costs
#  of shipment.
